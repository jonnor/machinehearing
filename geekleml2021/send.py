
import os

import requests


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
    assert r.status_code == 200, r.status_code

def main():

    url = os.environ.get("BREWFATHER_URL")
    device = os.environ.get("BREWFATHER_DEVICE")
    interval = int(os.environ.get("BREWFATHER_INTERVAL", "15"))

    brewfather_send(url, device, bpm=100)
    print("Sent")

if __name__ == '__main__':
    main()

