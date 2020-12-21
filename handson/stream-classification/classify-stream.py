
import argparse
import queue
import sys
import datetime

import matplotlib.pyplot as plt
import numpy
import sounddevice

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import inference as yamnet 

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger("tensorflow").addHandler(logging.NullHandler(logging.ERROR))

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def parse():

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    parser.add_argument(
        'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
        help='input channels to plot (default: the first)')
    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-r', '--samplerate', type=float, help='sampling rate of audio device')

    parser.add_argument(
        '--overlap', type=float, default=0.5,
        help='how much overlap between consequctive windows to classify')

    args = parser.parse_args()
    if any(c < 1 for c in args.channels):
        parser.error('argument CHANNEL: must be >= 1')

    return parser, args



def main():
    parser, args = parse()

    print('list')

    if args.list_devices:
        print(sounddevice.query_devices())
        parser.exit(0)

    if args.samplerate is None:
        device_info = sounddevice.query_devices(args.device, 'input')
        args.samplerate = device_info['default_samplerate']


    mapping = [c - 1 for c in args.channels]  # Channel numbers start with 1
    q = queue.Queue()

    def audio_callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)

        # Fancy indexing with mapping creates a (necessary!) copy:
        q.put(indata[:, mapping])
        #print(indata.shape)

    stream = sounddevice.InputStream(
        device=args.device, channels=max(args.channels),
        samplerate=args.samplerate, callback=audio_callback)

    print('stream open', args.device, stream)

    assert args.samplerate == 16000
    n_samples = int(args.samplerate*0.960*1.05)
    hop_length = n_samples * (1-args.overlap)
    new_samples = 0

    audio_buffer = numpy.zeros(shape=(n_samples,))

    model = yamnet.Model()

    import keras
    import tensorflow

    with stream:
        while True:
            data = q.get()
            data = numpy.squeeze(data)
            
            #print(data.shape)
            # move existing data over
            audio_buffer = numpy.roll(audio_buffer, len(data), axis=0)
            # add the new data
            audio_buffer[len(audio_buffer)-len(data):len(audio_buffer)] = data

            # check if we have received enough new data to do new classification
            new_samples += len(data)
            if new_samples >= hop_length:
                t = datetime.datetime.now()

                new_samples = 0
    
                waveform = audio_buffer

                with model.graph.as_default():
                    #x = numpy.reshape(waveform, [1, -1])
                    x = numpy.expand_dims(waveform, 0)
                    #x = numpy.expand_dims(x, -1)

                    scores, _spec, embeddings = model.yamnet.predict(x, steps=1, batch_size=1)

                    # Report the highest-scoring classes and their scores.
                    prediction = numpy.mean(scores, axis=0)
                    top_n = 3                   
                    top = numpy.argsort(prediction)[::-1][:top_n]

                    def format_pred(i):
                        return '  {:12s}: {:.3f}'.format(model.class_names[i], prediction[i])

                    if numpy.max(prediction) > 0.3:

                        print('classify', t)
                        print('\n'.join(format_pred(i) for i in top))


    print('stopped')

if __name__ == '__main__':
    main()
