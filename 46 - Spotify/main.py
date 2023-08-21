import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

URL_BASE = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "7fa91da6f0364e39a46d45c459b9b3ce"
CLIENT_SECRET = ""

# Pedir fecha al usuario en formato DD/MM/AAAA
fecha_input = input("Which year do you want to travel to? Type the date in this format (DD/MM/AAAA): ")
fecha = datetime.strptime(fecha_input, "%d/%m/%Y")
fecha_formateada = fecha.strftime("%Y-%m-%d")

url_complete = f"{URL_BASE + fecha_formateada}/"
response = requests.get(url_complete)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Find the top song and artist elements
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Extract the text from the elements
if song_names_spans:
    top_song_element = song_names_spans[0]
    top_song = top_song_element.getText().strip()

    top_artist_element = top_song_element.find_next_sibling("span", class_="c-label")
    top_artist = top_artist_element.getText().strip()

    print(f"The number one song on {fecha_formateada} is: {top_song} by {top_artist}")

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri="http://example.com",
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path="token.txt"))

    user_id = sp.current_user()["id"]
    playlist_name = f"{fecha_formateada} Billboard 100"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

    playlist_id = playlist["id"]
    print(f"Playlist created: {playlist['name']}")

    song_uris = []

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{fecha.year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    sp.playlist_add_items(playlist_id, song_uris)
    print("Songs added to the playlist.")

else:
    print("No information found for the provided date.")
