import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    
for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_artists(time_range=sp_range, limit=50)
    # print(results['items'])
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['genres'])

# top_artist = sp.current_user_top_artists(limit=20, offset=5)
# print(top_artist)
# top_songs = sp.current_user_top_tracks()
# print(top_songs)