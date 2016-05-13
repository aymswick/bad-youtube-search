from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import os, re, sys, argparse, time

def render(output_file):
	n = 1
	path = os.getcwd() + '/temp/' #THIS IS IMPORTANTS
	for i in os.listdir('temp'):
	    if i != '.DS_Store':
		os.rename(path + i, path + str(n) + '.mp4')
		n += 1

	# Load the image specifying the regions.
	im = ImageClip("./badlayout.png")

	# Loacate the regions, return a list of ImageClips
	regions = findObjects(im)


	# Load 5 clips
	clips = [VideoFileClip(n, audio=True).subclip(11,41) for n in
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
	cc.resize(0.6).write_videofile(output_file, fps=30)

	# Note that this particular composition takes quite a long time of
	# rendering (about 20s on my computer for just 4s of video).

if __name__ == "__main__":
	timestr = time.strftime("%Y-%m-%d_%H%M%S")
	default_outpath = './badvideos/'+ timestr +'.mp4'
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', default='./badvideos/'+timestr+'.mp4')
	args = parser.parse_args()
	#args.output
	print('output: ' + str(args.output))
	if args.output == './badvideos/.mp4':
		args.output = default_outpath
	render(args.output)
	os.system('xdg-open "'+str(args.output)+'"')
