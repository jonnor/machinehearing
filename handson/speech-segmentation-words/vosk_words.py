
import sys
import os
import subprocess
import json
import math

# tested with VOSK 0.3.15
import vosk
import librosa
import numpy
import pandas



def extract_words(res):
   jres = json.loads(res)
   if not 'result' in jres:
       return []
   words = jres['result']
   return words

def transcribe_words(recognizer, bytes):
    results = []

    chunk_size = 4000
    for chunk_no in range(math.ceil(len(bytes)/chunk_size)):
        start = chunk_no*chunk_size
        end = min(len(bytes), (chunk_no+1)*chunk_size)
        data = bytes[start:end]

        if recognizer.AcceptWaveform(data):
            words = extract_words(recognizer.Result())
            results += words
    results += extract_words(recognizer.FinalResult())

    return results

def main():

    vosk.SetLogLevel(-1)

    audio_path = sys.argv[1]
    out_path = sys.argv[2]

    model_path = 'vosk-model-small-de-0.15'
    sample_rate = 16000

    audio, sr = librosa.load(audio_path, sr=16000)

    # convert to 16bit signed PCM, as expected by VOSK
    int16 = numpy.int16(audio * 32768).tobytes()

    # XXX: Model must be downloaded from https://alphacephei.com/vosk/models
    # https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip
    if not os.path.exists(model_path):
        raise ValueError(f"Could not find VOSK model at {model_path}")

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)

    res = transcribe_words(recognizer, int16)
    df = pandas.DataFrame.from_records(res)
    df = df.sort_values('start')

    df.to_csv(out_path, index=False)
    print('Word segments saved to', out_path)

if __name__ == '__main__':
    main()

