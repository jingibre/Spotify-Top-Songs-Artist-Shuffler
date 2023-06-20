import spotipy
from spotipy.oauth2 import SpotifyOAuth
from my_credentials import my_client_secret, my_client_id, my_redirect_uri
import json

scope = "playlist-modify-private"  # Set the required scope for your application


spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=my_client_id, client_secret=my_client_secret,
                                                    redirect_uri=my_redirect_uri))

mother_playlist_url = 'https://open.spotify.com/playlist/2v6P7XipO1bQ7IVrG7mY9B?si=bb04ad02e3fe47e5'

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

playlist = spotify.playlist_tracks(mother_playlist_url, limit=100)


tracks = playlist["items"]
while playlist["next"]:
    playlist = spotify.next(playlist)
    tracks.extend(playlist["items"])



# Assuming you have fetched the tracks list from the playlist
artists = set()
artist_ids = set()


for track in tracks:
    for artist in track['track']['artists']:
        artist_name = artist['name']
        artists.add(artist_name)

        artist_id = artist['id']
        artist_ids.add(artist_id)

# Now you have a set of unique artist names

print(artists)