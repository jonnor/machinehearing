
import sys
import os
import subprocess
import json

# tested with VOSK 0.3.15
import vosk
import pandas


def extract_words(res):
   jres = json.loads(res)
   if not 'result' in jres:
       return []
   words = jres['result']
   return words

def transcribe_words(recognizer, process):
    results = []
    block_size = 4000
    while True:
        data = process.stdout.read(block_size)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            words = extract_words(recognizer.Result())
            results += words
    results += extract_words(recognizer.FinalResult())

    return results

def main():

    vosk.SetLogLevel(-1)

    audio_path = sys.argv[1]
    model_path = 'vosk-model-small-de-0.15'
    sample_rate = 16000

    if not os.path.exists(model_path):
        raise ValueError(f"Could not find VOSK model at {model_path}")

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)

    # TODO: replace ffmpeg with librosa/soundfile
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                                audio_path,
                                '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                                stdout=subprocess.PIPE)

    res = transcribe_words(recognizer, process)
    df = pandas.DataFrame.from_records(res)
    df = df.sort_values('start')
    print(df)

main()

