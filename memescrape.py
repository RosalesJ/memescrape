import praw
import urllib
import uuid
import re
import os
import time
working_dir = os.getcwd() + '/temp/'
creds = open("creds.csv",'r').read().split(",")
subreddits = ['me_irl','meirl','surrealmemes','deepfriedmemes']
reddit = praw.Reddit(client_id=creds[0],
                     client_secret=creds[1],
                     username=creds[2],
                     password=creds[3],
                     user_agent="memescrape")
try:
	while True:
		print("Refreshing le memes")
		for post in [x.url for x in reddit.subreddit('+'.join(subreddits)).top("day") if x.url.endswith(('.jpg','png'))]:
			print('Downloading: %s...'%(post))
			try:
				urllib.request.urlretrieve(post,working_dir+post.split('/')[-1])
			except urllib.error.HTTPError as e:
				print("Error")
		print("Done")
		time.sleep(3600)
		os.system("rm " + working_dir + "*")
		print("Refreshing...")
except KeyboardInterrupt as e:
	print("\nExiting")
