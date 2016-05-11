# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#Bad Youtube Search - Python 3
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from gdata import *
from badgui import *
#from badsort import *
from YOURAPIKEY import APIKEY
import sys
import youtube_dl


DEVELOPER_KEY = APIKEY # Dynamically updated via input box
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MAX_RESULTS = 50

class VideoObject:
    videoID = ""
    dislikeCount = 0
    likeCount = 0
    viewCount = 0
    factor = 0.0

    def __init__(self, videoID, dislikeCount, likeCount, viewCount):
        self.videoID = videoID
        self.dislikeCount = dislikeCount
        self.likeCount = likeCount
        self.viewCount = viewCount
        self.factor =  ((dislikeCount / likeCount) * viewCount) * 100
    def __rpr__(self):
        return rpr((self.id, self.dislikeCount))

def downloadWorst(worstVids):
    #Need to save videos as 1,2,3,4,5 in /temp/ folder
    #Need to for loop through all vids in list
    ydl_opts = {'format': 'worst/mp4', 'outtmpl': './temp/%(title)s.%(ext)s'}

    for vid in worstVids:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['http://www.youtube.com/watch?v=' + vid.videoID])


def youtube_search(keyword):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  global MAX_RESULTS
  videoTitles = []
  videoIds = []
  videoList = []
  get_stats = []
  dislikes = []

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
  #Change algorithm to dislikecount / viewcount
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
              try:
                  dislikes = int(stat_result["statistics"]["dislikeCount"])
                  likes = int(stat_result["statistics"]["likeCount"])
                  views = int(stat_result["statistics"]["viewCount"])
                  vid = VideoObject(ID, dislikes, likes, views)
                  videoList.append(vid)
                  break

              except:
                  count -= 1
              if(count == MAX_RESULTS):
                  break;


  #Print stuff
  videoList = sorted(videoList, key=lambda video: video.dislikeCount, reverse=True)

  for video in videoList:
      print('ID: ' + str(video.videoID))
      print('Dislikes: ' + str(video.dislikeCount))
      print('Likes: ' + str(video.likeCount))
      print('Views: ' + str(video.viewCount))
    # print('Factor: ' + str(video.factor))
      print('\n')

  os.system('rm -r temp/')
  downloadWorst(videoList[:5])
  os.system('python badrender.py')
  os.system('xdg-open temp/composition.mp4')
