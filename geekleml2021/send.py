
import time
import os

import requests
import structlog

log = structlog.get_logger()

import beerbubble

def brewfather_send(url, device, bpm, **kwargs):
    """
    See https://docs.brewfather.app/integrations/custom-stream
    """

    data = {
        "name": device,
        "bpm": bpm,
    }
    for k, v in kwargs.items():
        data[k] = v

    r = requests.post(url, json=data)
    #assert r.status_code == 200, r.status_code
    return r

def main():

    url = os.environ.get("BREWFATHER_URL")
    device = os.environ.get("BREWFATHER_DEVICE")
    interval = int(os.environ.get("BREWFATHER_INTERVAL", "15"))

    start = int(os.environ.get("BREWFATHER_START", "0"))

    f = beerbubble.synthesize_fermentation_rate()

    intervals = f.resample(f'{interval}min').mean().interpolate()
    

    for idx, i in intervals.iterrows():

        bpm = i.frequency
        error = None
        status = None
        try:
            pass
            r = brewfather_send(url, device, bpm=bpm)
            status = r.status_code
        except Exception as e:
            error = e
            pass        

        log.info("bpm-sent", time=idx, bpm=bpm, status=status, error=error)

        time.sleep(interval*60)

        #print("Sent")

if __name__ == '__main__':
    main()

