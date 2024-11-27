from datetime import datetime, time
from pprint import pprint
import requests
from bs4 import BeautifulSoup 
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import time

ID = ""
SECRET = ""

def ask_for_date():

    date_formats = [
        "%Y-%m-%d",  # YYYY-MM-DD
        "%d/%m/%Y",  # DD/MM/YYYY
        "%m/%d/%Y",  # MM/DD/YYYY
        "%d-%m-%Y",  # DD-MM-YYYY
        "%m-%d-%Y",  # MM-DD-YYYY
        "%d.%m.%Y",  # DD.MM.YYYY
        "%m.%d.%Y",   # MM.DD.YYYY
        "%Y.%m.%d.",
        "%Y.%m.%d"
    ]

    valid_date = None  

    # runs until a valid date format found
    while not valid_date:
        travel_date = input("What year would you like to travel to? (Enter in YYYY-MM-DD format): ")

        for date_format in date_formats:
            try:
                # Convert date
                time.sleep(0.1)
                valid_date = datetime.strptime(travel_date, date_format)
                break  
            except ValueError:
                continue  

        if not valid_date:
            print("Invalid date format. Please try again.")

    formatted_date = valid_date.strftime("%Y-%m-%d")

    return formatted_date

def create_spotify_list(date ,year, track_list, artist_list):
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=ID,
        client_secret=SECRET,
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-private"
    ))

    user_id = sp.current_user()["id"]

    # Create playlist
    playlist_name = f"Billboard TOP 100 HITS {date}"
    playlist_description = f"List of the top 100 tracks of {date}, from billboard.com/charts, made for testing my programming skills\nIt won't be always 100 tracks, some song can not be found on spotify\n\nDisclaimer: it is made for learning how to us spotify api, not for money making. If you find it unethical, please contact me (tesztlajos5@gmail.com), and I will remove it"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)
    time.sleep(0.1)

    print(f"Lejátszási lista létrehozva: {playlist['name']}")

    track_ids = []
    time.sleep(1)
    # Add to playlist
    for track, artist in zip(track_list, artist_list):
        # find track
        query = f"track:{track} artist:{artist}"
        result = sp.search(q=query, type="track", limit=1)
        time.sleep(0.1)
        # try out with adding it to our list
        try:
            track_ids.append(result['tracks']['items'][0]['uri'])
            print(f"Hozzáadva {track} - {artist}")
        except IndexError:
            print(f"Nem található: {track} - {artist}")

    # add tracks to playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_ids)

    print("A dalok sikeresen hozzáadva a privát lejátszási listához!")
        
def main():
    date = ask_for_date()
    #date = "2000-10-07"

    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    web_page = response.text

    soup = BeautifulSoup(web_page, "html.parser")

    # Scrape track titles
    titles = soup.select("li ul li h3")
    titles_list = [title.text.strip() for title in titles]
    # Scrape artist names
    artists = soup.select("ul li ul li span")
    artist_list_unfiltered = [artist.text.strip() for artist in artists]
    artist_list_filtered = [artist_list_unfiltered[0].split("Featuring")[0].strip()] + \
                           [artist.split("Featuring")[0].strip() for artist in artist_list_unfiltered[7::7]]    
    #pprint(artist_list_filtered)

    create_spotify_list(date=date, year=date[:4],track_list=titles_list, artist_list=artist_list_filtered)

main()
