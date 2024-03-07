import time
from models.tracks import track
import requests
import json

def play(track_name):
    tracks = track.list_tracks()
    if track_name in tracks:
        print(f"START PLAY {track_name}")
        for x in range(10):
            print("la la la")
            time.sleep(1)
    print("track not found")
    
    
def download(url):
    response = requests.get(url)
    data = response.text
    print(data)
    track.save(data, "no name")