import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

current_user = sp.current_user()
current_user_display_name = current_user['display_name']
current_user_id = current_user['id']
# print(current_user)


artist= 'Crystal Castles'
track= 'Kerosene'

track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
print(track_id['tracks']['items'][0])