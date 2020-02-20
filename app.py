import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='2pac', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'],track['duration_ms'])
    #print(results)