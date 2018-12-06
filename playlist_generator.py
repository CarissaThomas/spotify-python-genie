import spotipy.util as util
import spotipy
import sys

sp = {}
username_id = ""


def setCredentials(creds, username):
    global sp
    global username_id
    username_id = username
    sp = creds
    show_related_artists(input("Artist name please: "))


def show_recommendations_for_artist(artist_id):
    results = sp.recommendations(seed_artists=artist_id, limit=30)
    track_ids = []

    for track in results['tracks']:
        track_ids.append(track['id'])

    return track_ids


def show_related_artists(artist):
    result = sp.search(q=artist, type='artist')

    try:
        uri = result['artists']['items'][0]['uri']

        related = sp.artist_related_artists(uri)

        for artist in related['artists']:
            track_ids = show_recommendations_for_artist([artist['id']])

        createPlaylist(track_ids)  # Create the new playlist to be populated
        print("Playlist created!!")
    except Exception as e:
        print(e)


def createPlaylist(track_ids):
    playlist_name = input("Create a new playlist name: ")
    sp.trace = False
    playlist = sp.user_playlist_create(
        user=username_id, name=playlist_name, public=True)
    addToPlaylist(playlist['id'], track_ids)
    return


def addToPlaylist(playlist_id, track_ids):
    results = sp.user_playlist_add_tracks(
        user=username_id, playlist_id=playlist_id, tracks=track_ids)
    return
