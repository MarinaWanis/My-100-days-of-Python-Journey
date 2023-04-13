from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year= date.split("-")[0]
month= date.split("-")[1]
day = date.split("-")[2]
URL= f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"

response = requests.get(url=URL)
html_songs = response.text


soup = BeautifulSoup(html_songs, "html.parser")
titles_list = [song.getText().strip("\n\t") for song in soup.select(selector="li h3", class_="c-title")]
# print(soup.prettify())
song_titles = titles_list[0:100]
print(song_titles)
# print(artists_list)


CLIENT_ID = "24299a0e3d094f55aa0c0493d7f5a20e"
CLIENT_SECRET = "ccf3268662ae4c2dabce32dcdfeb09a7"
REDIRECT_URI = "http://localhost:8080"
SPOTIFY_ENDPOINT= "https://api.spotify.com/v1"

scope = "playlist-modify-private",
redirect_uri = "http://example.com",


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI,show_dialog = True,
cache_path = "token.txt"))

song_uris= []

playlist_header ={
    "Authorization": f"Bearer {sp}"
}

playlist_params= {
    "name":f"{date} Billboard 100",
    "description": "My new Playlist",
    "public": False
}

print(song_titles)

for song in song_titles:
    result = sp.search(f"track:{song} year:{year}", type="track")
    try:
        uri =result["tracks"]["items"][0]["uri"]
        # print(result)
    except IndexError:
        # print("Song URI not found")
        pass
    else:
        # uri =uri.split(":")[2]
        song_uris.append(uri)
        track_uri = uri
        track_id = track_uri.split(':')[-1]  # Extract the track ID from the URI
        try:
            track_info = sp.track(track_id)
            print(f"Track {track_info['name']} by {track_info['artists'][0]['name']} is valid!")
        except spotipy.SpotifyException as e:
            print(f"Track with URI {track_uri} is invalid: {e}")

playlist = sp.user_playlist_create(user="09rurify0b46k51doxaz9pue1", name=f"{date} Billboard 100 v3", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

