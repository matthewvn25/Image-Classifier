
import praw
import datetime
import urllib
import requests

reddit = praw.Reddit(client_id = '6oQuWT8j5mrj0g', 
                     client_secret = 'lwCsLOu6b9Doayj96CHyuCWJo0fVtg', 
                     user_agent = 'GeminiScraper')

image_urls = []
for post in reddit.subreddit("AnimeWallpaper").new(limit=10):
    image_urls.append(post.url.encode('utf-8'))
    
print(image_urls)
response = requests.get(image_urls[0])
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

#print(submission.title)

# subreddit = reddit.subreddit('animewallpaper') 
# posts = subreddit.hot(limit=10)

# image_urls = []
# image_titles = []
# image_scores = []
# image_timestamps = []
# image_ids = []


# for post in posts:
#   image_urls.append(post.url.encode('utf-8'))
#   image_titles.append(post.title.encode('utf-8'))
#   image_scores.append(post.score)
#   image_timestamps.append(datetime.datetime.fromtimestamp(post.created))
#   image_ids.append(post.id)

# print(image_titles)
