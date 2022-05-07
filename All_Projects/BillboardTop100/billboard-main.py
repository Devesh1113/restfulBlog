from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["CLIENT_ID"],
                                               client_secret=os.environ["CLIENT_SECRET"],
                                               redirect_uri="https://deveshnice2.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path=".cache"))

current_user_id = sp.current_user()["id"]
print(current_user_id)

ask_time = input("What year you would like to travel to? Type "
                 "the date in YYYY-MM-DD format")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{ask_time}/")
data = response.text

soup = BeautifulSoup(data, 'html.parser')

songs_title = soup.find_all(name='h3', class_='a-no-trucate', id='title-of-a-story')

song_list = [song.getText().split('\n')[1] for song in songs_title]
year = ask_time.split("-")[0]

songs_uri_list = []
for song in song_list:
    results = sp.search(q=f"track: {song} year: {year}", type="track")

    try:
        song_uri = results["tracks"]["items"][0]["uri"]
        songs_uri_list.append(song_uri)
    except IndexError:
        print(f"{song} doesn't exist in Spoitfy. Skipped")

playlist = sp.user_playlist_create(user=current_user_id, name=f"{ask_time}BillBoard100", public=False)
print(playlist["id"])

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri_list)

