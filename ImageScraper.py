
import praw
import datetime
import urllib
import requests

reddit = praw.Reddit(client_id = '6oQuWT8j5mrj0g', 
                     client_secret = 'lwCsLOu6b9Doayj96CHyuCWJo0fVtg', 
                     user_agent = 'GeminiScraper')

image_urls = []
for post in reddit.subreddit("AnimeWallpaper").new(limit=1):
    image_urls.append(post.url.encode('utf-8'))
    
print(image_urls)
response = requests.get(image_urls[0])
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

