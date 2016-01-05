# ==========================================================================================================

# Wallpaperer 
# [Tue Jan  5 19:14:10 IST 2016]

# Rohan Gulati
# rohangulati[at]gmail.com
# github.com/rohan-gulati

# Small python script that fetches images from the SFW Network on reddit using PRAW (Python Reddit API Wrapper) 
# and changes the Desktop wallpaper.

# Usage: python wp.py

# ==========================================================================================================

# Libraries
import praw
import requests
import wget
import os
import random

# ==========================================================================================================

# Add your subs to this list. Subs without a sticky/self first post work best.
subs = ['EarthPorn', 'F1Porn', 'CarPorn', 'MilitaryPorn', 'HistoryPorn']

user_agent = 'Wallpaperer 1.0 by Rohan Gulati | github.com/rohan-gulati'

randNumber = random.randint(0,len(subs)-1)
subreddit = subs[randNumber]

try:
	# Directory where the wallpaper is stored.
	outDir = '/home/rohan/FOOBAR/Wallpaperer/walls/'

	newRedditInstance = praw.Reddit(user_agent=user_agent)
	subObj = newRedditInstance.get_subreddit(subreddit)
	postsObj = subObj.get_hot(limit=10)

	imgObj = [x for x in postsObj]
	sObj = imgObj[random.randint(0, 9)]

	if(not(x.is_self)):
		try:
			print "Fetching a fresh wallpaper from " + str(subObj)
			print "\n" + str(sObj.title)
		except UnicodeEncodeError:
			print "Fetching a wallpaper..."
		os.chdir("/home/rohan/FOOBAR/Wallpaperer/walls/")
		pwd = os.getcwd()

		# Clean up directory to prevent duplicates
		files = os.listdir(pwd)
		for f in files:
			os.remove(os.path.join(pwd,f))
		
		wget.download(sObj.url)
		files = os.listdir(pwd)
		fileName = str(files[0])
		
		if fileName.endswith(".jpg"):
			sysCommand = "gsettings set org.gnome.desktop.background picture-uri file:///home/rohan/FOOBAR/Wallpaperer/walls/%s" % (fileName)
			os.system(sysCommand)

except requests.ConnectionError:
	print "No internet bbz :("
