import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import wget 
import sys

#search Spotify for desired artist, copy URI, and input below:
artist_uri = 'spotify:artist:INSERT URI HERE'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(artist_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

url_list = []

for album in albums:
    url_list.append(album['images'][0]['url'])
    
#set desired directory output below:
for x in range(len(url_list)): 
   print(wget.download(url_list[x], out='C:/Users/' and 'albumcover.jpeg'))