from __future__ import unicode_literals
print("Importing all libraries...")
import requests
import os
import sys

try:
    import youtube_dl
except ModuleNotFoundError:
    print("Installing youtube_dl...")
    os.system("pip install youtube_dl")
    os.execl(sys.executable, sys.executable, * sys.argv)

print("Done!")

try:
    api_key = sys.argv[1]
    playlistId = sys.argv[2]
    savedir = sys.argv[3]
except IndexError:
    api_key = input("API Key: ")
    playlistId = input("Playlist ID: ")
    savedir = input("Save dir with backslash at path end (Write ./ for save here " + os.getcwd() + "\ ): ")



ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': savedir + '%(title)s.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}



url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults=50&playlistId=" + playlistId + "&key=" + api_key

r = requests.get(url)

data = r.json()
for item in data["items"]:
    link = "https://www.youtube.com/watch?v=" + item["snippet"]["resourceId"]["videoId"]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])