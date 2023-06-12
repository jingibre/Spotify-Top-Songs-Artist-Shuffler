import spotipy
from spotipy.oauth2 import SpotifyOAuth
from my_credentials import my_client_secret, my_client_id, my_redirect_uri

scope = "playlist-read-private"  # Set the required scope for your application


spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=my_client_id, client_secret=my_client_secret,
                                                    redirect_uri=my_redirect_uri))


lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

results = spotify.artist_top_tracks(lz_uri)
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()