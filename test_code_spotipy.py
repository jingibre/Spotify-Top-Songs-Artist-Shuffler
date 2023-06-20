import spotipy
from spotipy.oauth2 import SpotifyOAuth
from my_credentials import my_client_secret, my_client_id, my_redirect_uri
import random
from tqdm import tqdm
import json

scope = "playlist-modify-public"  # Set the required scope for your application


spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=my_client_id, client_secret=my_client_secret,
                                                    redirect_uri=my_redirect_uri, scope=scope))

mother_playlist_url = 'https://open.spotify.com/playlist/2v6P7XipO1bQ7IVrG7mY9B?si=bb04ad02e3fe47e5'
shuffled_playlist_url = 'https://open.spotify.com/playlist/3Dpt6EdPaPppkSK6d65ExT?si=b7b972972d2f4561'

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

playlist = spotify.playlist_tracks(mother_playlist_url, limit=100)


tracks = playlist["items"]
while playlist["next"]:
    playlist = spotify.next(playlist)
    tracks.extend(playlist["items"])



artists = set()
artist_ids = set()


# for track in tracks:
#     for artist in track['track']['artists']:
#         artist_name = artist['name']
#         artists.add(artist_name)
#
#         artist_id = artist['id']
#         artist_ids.add(artist_id)

# alternative with main artists only
for track in tracks:
    artist_name = track['track']['artists'][0]['name']  # Get the name of the first artist
    artists.add(artist_name)

    artist_id = track['track']['artists'][0]['id']
    artist_ids.add(artist_id)


# Now you have a set of unique artist names

print(artist_ids)
print(artists)

print(len(artists))


selected_new_songs = []

for artist_id in tqdm(artist_ids, desc="Processing artists"):
    results = spotify.artist_top_tracks(artist_id)
    top_10_songs = results['tracks'][:10]

    if len(top_10_songs) >= 2:
        selected_new_songs.extend(random.sample(top_10_songs,2))
    else:
        selected_new_songs.extend(top_10_songs)


# songs to add

# Extract the track URIs from the top songs
track_uris = [song['uri'] for song in selected_new_songs]

print(track_uris)

# Clear the existing tracks from the playlist
spotify.playlist_replace_items(shuffled_playlist_url, [])

# Extract the track URIs from the top song
# Add the tracks to the playlist
# get

def add_tracks_to_playlist(playlist_id, track_uris, batch_size: int = 100):
    num_batches = len(track_uris) // batch_size + 1

    for i in tqdm(range(num_batches), desc='Adding Tracks'):
        batch = track_uris[i * batch_size : (i + 1) * batch_size]  # Get a batch of track URIs
        spotify.playlist_add_items(playlist_id, batch)

add_tracks_to_playlist(shuffled_playlist_url, track_uris, batch_size=50)