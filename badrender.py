from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import os, re


n = 1
path = os.getcwd() + '/temp/' #THIS IS IMPORTANTS
for i in os.listdir('temp'):
    if i != '.DS_Store':
        os.rename(path + i, path + str(n) + '.mp4')
        n += 1

# Load the image specifying the regions.
im = ImageClip("./mosaic_layout.png")

# Loacate the regions, return a list of ImageClips
regions = findObjects(im)


# Load 5 clips
clips = [VideoFileClip(n, audio=False).subclip(11,41) for n in
     [ "./temp/1.mp4",
      "./temp/2.mp4",
      "./temp/3.mp4",
      "./temp/4.mp4",
      "./temp/5.mp4"]]

# fit each clip into its region
comp_clips =  [c.resize(r.size)
                .set_mask(r.mask)
                .set_pos(r.screenpos)
               for c,r in zip(clips,regions)]

cc = CompositeVideoClip(comp_clips,im.size)
cc.resize(0.6).write_videofile("./temp/composition.mp4", fps=30)

# Note that this particular composition takes quite a long time of
# rendering (about 20s on my computer for just 4s of video).
