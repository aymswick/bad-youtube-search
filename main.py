#Bad Youtube Search - Python 3
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from gdata import *
import sys
from badgui import *
from badsort import *
from YOURAPIKEY import APIKEY


DEVELOPER_KEY = APIKEY # Dynamically updated via input box
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
    maxResults=50 #THIS NUMBER DETERMINES HOW MANY VIDEOS ARE RETURNED
  ).execute()

  videoTitles = []
  videoIds = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
          videoTitles.append(search_result["snippet"]["title"])
          videoIds.append(search_result["id"]["videoId"])
          #search_result["statistics"]["likeCount"]

      elif search_result["id"]["kind"] == "youtube#channel":
          channels.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["channelId"]))

      elif search_result["id"]["kind"] == "youtube#playlist":
          playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                  search_result["id"]["playlistId"]))

  #print("Videos:\n", "\n".join(videos), "\n")
  print "Channels:\n", "\n".join(channels), "\n"
  print "Playlists:\n", "\n".join(playlists), "\n"

  for video in videoIds:
      print(video)
