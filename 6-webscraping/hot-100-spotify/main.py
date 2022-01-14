from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
TOKEN_PATH = "ADD_PATH_TO_TOKEN.TXT_HERE"

def get_songs():
    URL = "https://www.billboard.com/charts/hot-100/"
    global date
    # Adds date to url
    date_url = URL + date

    # Requests html page and makes soup
    response = requests.get(date_url)
    hot_100_html = response.text
    soup = (BeautifulSoup(hot_100_html, "lxml"))

    # Finds Song names and appends to music list
    music_list = []
    first = soup.find('h3',
                      class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").getText()
    music_list.append(first.strip())

    others = soup.find_all('h3',
                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
    for tag in others:
        music_list.append(tag.getText().strip())
    return music_list

# Input of date requested
date = input("Choose a date in the format YYYY-MM-DD: ")
song_titles = get_songs()

# Starts spotidy module
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=TOKEN_PATH
        )
)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]

# Searches and adds songs to uri's to list
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"'{song}' doesn't exist in Spotify. Skipped.")

# Creates playlist
playlist = sp.user_playlist_create(user=user_id,
                                      name=f'{date} HOT 100',
                                      public=False)

# Adds songs with uri's list
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
