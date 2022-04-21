
# AudioStreamer 

Universal streaming audio input.
Transparent support for live streams and stored files, both locally and remote.


## Usage examples
Should be runnable and show key concepts.

- Visualizer of soundlevel/spectrum. Live/animated
- Compute features, output to CSV file
- Run an audio classifier. Ie Audioset classes
- Streaming normalization. For example spectral subtraction
- Storing audio to disk

## Sources

- Audio files. In all the common formats .WAV/.mp3/.m4a/.aac/.flac/.ogg
- Audio from microphone. Anything that OS shows as input device. Linux/Mac/Windows
- Audio stream. Such as web radio with HTTP/Icecast or webcam with RTP/RTSP 
- Video stream, via HTTP. Youtube live
- Video file. Via HTTP. Locally

## Features

Support overlap. Default to 0% ?
Support handling incomplete frames.
At end-of-stream etc. Strategy: padding/cropping or dropping 


## Maybe

## Support resampling?
Allowing to specify desired samplerate
Benefit to have it responsibility of generator when sources allow selecting stream with compatible,
like some video hosting services (youtube etc).

## Multiple files/streams?
Like directories of audio files. With a glob etc
Does Receiver needs to handle multiple stream contexts?
Might be better to have multiple receivers. Like a pool of workers. Each gets their own audio queue (and process)
Quite rare to mix data from streams, normally treated independently.
Possible exception: stereo/multi-channel sound

## Support multi-processing?
In particular for off-line cases, to speed up batch workloads on whole datasets
Especially splitting on file/stream level
But potentially also inside a stream.


## Support other traversals than in-order?
Randomize only traversal of streams, in-order inside stream
Randomize both window selection inside stream 

Enables ML model training uses, tends to do batches with samples from a whole dataset
Though often is not random selection per-batch, just "shuffling" order before each epoch

## Support to specify sub-sampling?
Regular spacing
Uniform random

## API

- Pass a Receiver instance to the Generator
- Generator calls Receiver, on each new window.
Also hooks for start/end of stream.
And start/end of entire set of streams.
- Generator may run free-standing
or need to be regularly called to poll stream forward

On each window
    Samples
    Identifiers:
        File/stream identifier
        Window/time identifier

When creating generator:

Must specify number of samples in window.


## Implementation

Build on existing libraries

- soundfile, for local files
- sounddevice, for microphone input
- fsspec - for remote files
- youtube-dl, for Youtube and related
- ffmpeg, for streaming from RTP etc

Considerations

- May need to use threads/processes and queues internally
- May need to adapt between different buffer sizes used with the input source,
versus what the receiver is supposed to receive


## Outreach 

People that need this
https://stackoverflow.com/questions/67204592/python-get-audio-data-from-rtsp-stream
https://stackoverflow.com/questions/46542444/record-rtsp-stream-to-file-wav
https://stackoverflow.com/questions/69766148/is-there-a-way-to-stream-rtsp-audio-stream-only-to-stdout-with-ffmpeg
https://stackoverflow.com/questions/19280551/how-to-work-rtsp-in-python
https://stackoverflow.com/questions/68868095/getting-rtp-audio-into-a-numpy-ndarray

