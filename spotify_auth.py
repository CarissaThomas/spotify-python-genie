import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import playlist_generator
import sys
import spotipy.util as util
import os
from json.decoder import JSONDecodeError

creds = SpotifyClientCredentials()

if __name__ == '__main__':

    try:
        token = util.prompt_for_user_token(username=creds.username, scope='playlist-modify-public', client_id=creds.client_id,
                                           client_secret=creds.client_secret, redirect_uri="http://localhost:5000/")

    except (AttributeError, JSONDecodeError):  # work around for current cache bug
        os.remove(f".cache-{creds.username}")
        token = util.prompt_for_user_token(username=creds.username, scope='playlist-modify-public', client_id=creds.client_id,
                                           client_secret=creds.client_secret, redirect_uri="http://localhost:5000/")

    if token:
        auth = spotipy.Spotify(auth=token)
        playlist_generator.setCredentials(auth, creds.username)
