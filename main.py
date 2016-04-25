#Bad Youtube Search - Python 3
from tkinter import *
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import sys

DEVELOPER_KEY = '' # Dynamically updated via input box
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(keyword):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=25 #THIS NUMBER DETERMINES HOW MANY VIDEOS ARE RETURNED
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
          videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))

      elif search_result["id"]["kind"] == "youtube#channel":
          channels.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["channelId"]))

      elif search_result["id"]["kind"] == "youtube#playlist":
          playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                  search_result["id"]["playlistId"]))

  print("Videos:\n", "\n".join(videos), "\n")
  print("Channels:\n", "\n".join(channels), "\n")
  print("Playlists:\n", "\n".join(playlists), "\n")

def onClick():
    DEVELOPER_KEY = apiBox.get()
    youtube_search(entryBox.get())


#Run this on application create
app = Tk()
app.title("Bad Youtube Search")
app.geometry("600x400")
app.configure(bg="#8f8f8f")

#Input Box
entryBox = Entry(app, font=("Roboto", 24), fg="#5e5e5e", justify="center" )
apiBox = Entry(app, font=("Roboto", 12), fg="#5e5e5e", justify="center")

#Send Button
sendButton = Button(app, font="Roboto", text="Search", width="300", height=5,
                    bd=0, bg="#c0392b", fg="#ffffff", activeforeground="#ffffff" ,activebackground="#e74c3c", justify="center",
                    command=onClick)
entryBox.place(x=55, y=100, height=50, width=500)
apiBox.place(x=55, y=145, height=20, width=50)
sendButton.place(x=155, y=175, height=50, width=300)

app.mainloop()
