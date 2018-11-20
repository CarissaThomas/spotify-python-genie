import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy.util

credentials = SpotifyClientCredentials()

if __name__ == '__main__':
    username = input("Enter in your spotify username: ")

    loginPrompt = spotipy.util.prompt_for_user_token(
        username, scope=None, client_id=credentials.client_id, client_secret=credentials.client_secret, redirect_uri="http://spotifygenie.com")

# set up a user log in
