import json
import time

def list_tracks():
    """
    Ritorna la lista delle tracce.
    """
    tracks = []
    with open('db/db.json', 'r') as f:
        tracks = json.load(f)
    return sorted(tracks)

def save(data, name):
    print(f"salavato {name}")