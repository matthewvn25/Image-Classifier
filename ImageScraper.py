
#"pip install praw" in console to install praw
import praw
import urllib
import requests
import os.path
import time




if __name__ == "__main__":
    #Login infor to use Praw in reddit. Created and registered an app in reddit
    reddit = praw.Reddit(client_id = '6oQuWT8j5mrj0g',
                         client_secret = 'lwCsLOu6b9Doayj96CHyuCWJo0fVtg',
                         user_agent = 'GeminiScraper')
    
    image_urls = []
    #takes posts from subreddit and adds to list
    for post in reddit.subreddit("AnimeWallpaper").new(limit=10):
        #only adds if the file is a png or jpg
        #//todo: add more searches if post is not a picture
        if post.url[-4:] == '.png' or  post.url[-4:] == '.jpg':
            image_urls.append(post.url)
    
    
    
    #print(image_urls)
    #print(len(image_urls))
    
    
    #until UI this is how we will take user directory
    #folder = input("Enter the Name of the folder to save images")
    folder = 'Images/'
    #saves images to folder
    for x in range(len(image_urls)):
        imageName = image_urls[x].replace('https://',''). \
            replace('i.redd.it/','').replace('i.imgur.com/','').\
                replace('imgur.com/a/','')
        response = requests.get(image_urls[x])
        fullpath = os.path.join(folder,imageName)
        file = open(fullpath, "wb")
        file.write(response.content)
    file.close()
        
    for images in fullpath:
        print(images)
    
  

