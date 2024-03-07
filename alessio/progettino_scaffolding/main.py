import os  # libreria di sistema
import requests  # libreria esterna da installare
from models.tracks import track
from services.player import player

help = """
Questo programma blablabla

se premi R riproduci una canzone inserendone il nome
se premi D la scarichi da internet e la salvi sul database


"""

def main():
    tracks = track.list_tracks()
    for _track in tracks:
        print(_track)

    action = input("""
        Cosa vuoi fare?\n\n

        R = riproduci\n
        D = download
    """)

    if action == "R":
        track_name = input("che traccia vuoi riprodurre?")
        player.play(track_name)
    elif action == "D":
        url = input("inserisci la url")
        player.download(url)
    else:
        print(help)


main()
