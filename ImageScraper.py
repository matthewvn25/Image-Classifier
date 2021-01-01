
#"pip install praw" in console to install praw
import praw
import urllib
import requests
import os.path

#Login infor to use Praw in reddit. Created and registered an app in reddit
reddit = praw.Reddit(client_id = '6oQuWT8j5mrj0g',
                     client_secret = 'lwCsLOu6b9Doayj96CHyuCWJo0fVtg',
                     user_agent = 'GeminiScraper')

image_urls = []
#takes posts from subreddit and adds to list
for post in reddit.subreddit("AnimeWallpaper").new(limit=10):
    image_urls.append(post.url)


print(image_urls)
folder = 'Image/'
#saves images to folder
for x in range(len(image_urls)):
    imageName = image_urls[x]
    response = requests.get(image_urls[x])
    fullpath = os.path.join('Images/',str(imageName[-17:]))
    file = open(fullpath, "wb")
    file.write(response.content)
    file.close()

