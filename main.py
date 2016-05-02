#Bad Youtube Search - Python 3
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from gdata import *
from badgui import *
#from badsort import *
from YOURAPIKEY import APIKEY
import sys


DEVELOPER_KEY = APIKEY # Dynamically updated via input box
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MAX_RESULTS = 5

class VideoObject:
    def __init__(self, videoID, likeCount, dislikeCount):
        self.videoID = videoID
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
    def __rpr__(self):
        return rpr((self.id, self.dislikeCount))

def youtube_search(keyword):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  global MAX_RESULTS
  videoTitles = []
  videoIds = []
  videoList = []
  get_stats = []


  #INITIAL SEARCH, GET LIST OF VIDEOS
  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=MAX_RESULTS #THIS NUMBER DETERMINES HOW MANY VIDEOS ARE RETURNED
  ).execute()

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
          videoTitles.append(search_result["snippet"]["title"])
          videoIds.append(search_result["id"]["videoId"])

  #Call the statistics query for each video id returned from previous query
  for ID in videoIds:
       get_stats.append(youtube.videos().list(
       part="id,statistics",
       id= ID
       ).execute())

  count = 0
  for stats in get_stats: #Each list in get_stats has twice the number of items in it due to the part having both id and statistics
      for stat_result in stats.get("items", []):
          if stat_result["kind"] == "youtube#video":
              count += 1 #So, to solve this we manually break out after count of max_results
              ID = stat_result["id"]
              likes = stat_result["statistics"]["likeCount"]
              dislikes = stat_result["statistics"]["dislikeCount"]
              vid = VideoObject(ID, likes, dislikes)
              videoList.append(vid)
              if(count == MAX_RESULTS):
                  break;


  #Print stuff
  for video in videoList:
      #print('Title: ' + video.videoTitle)
      print('ID: ' + video.videoID)
      print('Likes: ' + video.likeCount)
      print('Dislikes: ' + video.dislikeCount)
      print('\n')
