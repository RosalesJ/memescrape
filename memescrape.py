import praw
import urllib
import uuid
import re
working_dir = '/Users/coby/Projects/memescrape/temp/'
creds = open("creds.csv",'r').read().split(",")
reddit = praw.Reddit(client_id=creds[0],
                     client_secret=creds[1],
                     username=creds[2],
                     password=creds[3],
                     user_agent="memescrape")
for post in [x.url for x in reddit.subreddit('me_irl').top('hour') if x.url.endswith('.jpg') or x.url.endswith('.png')]:
	print('Downloading: %s...'%(post))
	urllib.request.urlretrieve(post,working_dir+post.split('/')[len(post.split('/'))-1])
