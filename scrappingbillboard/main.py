from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "1e2cb2fa948746f3aba6abda1ebc73fe"
CLIENT_SECRET = "71cecdc2a67b493e8b2c7cec51f38873"

input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/"+input_date)
soup = BeautifulSoup(response.text,'html.parser')
song_names_spans = soup.find_all("span",class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user_()["id"]
print(user_id)
