import spotipy
import os
from dotenv import load_dotenv
load_dotenv()
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
pd.set_option('display.max_columns', None)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=f"{client_id}",
                                               client_secret=f"{client_secret}",
                                               redirect_uri="http://localhost:3000/callback",
                                               scope="user-library-read"))

taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
