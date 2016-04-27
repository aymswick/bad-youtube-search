class VideoObject:
    def __init__(self, videoID, dislikeCount):
        self.videoID = videoID
        self.dislikeCount = dislikeCount
    def __rpr__(self):
        return rpr((self.id, self.dislikeCount))
        
videoList = []

videoList.append(VideoObject(search_result["id"]["videoId"], search_result["statistics"]["dislikeCount"])

videoList = sorted(videoList, key=attrgetter('dislikeCount'), reverse=True)
print(videoList)
