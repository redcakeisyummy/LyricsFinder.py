import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius

# ——————————————————————————————


# 1. PUT YOUR API HERE:
SPOTIPY_CLIENT_ID = "CHANGE THIS" 
SPOTIPY_CLIENT_SECRET = "CHANGE THIS"
GENIUS_ACCESS_TOKEN = "CHANGE THIS"

# 2. INFO ABOUT YOUR MUSIC
TRACK_NAME = "MUSIC NAME"
ARTIST_NAME = "ARTIST NAME"


# ——————————————————————————————

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN, verbose=False, remove_section_headers=False)


try:
    print(f"🎵 Finding Lyrics For: {TRACK_NAME} By: {ARTIST_NAME}...")
    
    song = genius.search_song(TRACK_NAME, ARTIST_NAME)
    
    if song:
        print(f"\n--- ✨ Lyrics From: {song.title} By: {song.artist} ---")
        print(song.lyrics)
    else:
        print(f"\n❌ Cant Find Lyrics For: {TRACK_NAME} By: {ARTIST_NAME}")

except Exception as e:
    error_message = str(e)
    
    if "401" in error_message and "unauthorized" in error_message:
        print("\n!!!SPOTIFY API ERROR!!!")
        print("❌ CHECK YOUR Client ID or Client Secret AT LINE 9, 10")
    
    elif "401" in error_message and "invalid_token" in error_message:
        print("\n!!!GENIUS API ERROR!!!")
        print("❌ TOKEN ERROR, CHECK YOUR GENIUS TOKEN AT LINE 11")
        
    else:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
