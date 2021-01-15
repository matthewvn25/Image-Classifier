
#"pip install praw" in console to install praw
import praw
import urllib
import requests
import os.path
import time

###############################
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageChops
from numpy import asarray

import sys

#from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
###############################

#research eigen values
def similarityPercentage(imageLocation):
    # source = Image.open("Source.png")
    # img = Image.open(imageLocation)
    # absDiff = ImageChops.difference(source, img)
    # absDiff_pixel = absDiff.load()
    # zeroCount = 0
    
    # for i in range (absDiff.size[0]): # for each row in the image
    #     for j in range(absDiff.size[1]): # for each col in the image
    #         if(absDiff_pixel[i,j] == (0,0,0)):
    #             zeroCount = zeroCount + 1
    # similarityPercentage[imageName] = zeroCount * 100 / (absDiff.size[0] * absDiff.size[1])

    # for key in similarityPercentage:
    #     print(key + ": " + str(similarityPercentage[key]) + "%")
    # return similarityPercentage[key]
    return 1


if __name__ == "__main__":
    #Login infor to use Praw in reddit. Created and registered an app in reddit
    reddit = praw.Reddit(client_id = '6oQuWT8j5mrj0g',
                         client_secret = 'lwCsLOu6b9Doayj96CHyuCWJo0fVtg',
                         user_agent = 'GeminiScraper')
    

    folder = 'Waifu/'
    #Generates a list of posts on the subreddit that can be navigated
    #though one at a time
 
    postsListGenerator = reddit.subreddit("AnimeWallpaper").new(limit=1)
    for post in postsListGenerator:
        #if the post is an image
        if post.url[-4:] == '.png' or  post.url[-4:] == '.jpg':
            #download the image
            response = requests.get(post.url)
            #get the name of the image
            imageName = post.url.replace('https://',''). \
                replace('i.redd.it/','').replace('i.imgur.com/','').\
                    replace('imgur.com/a/','')
            #join the name and folder
            fullpath = os.path.join(folder,imageName)
            #open and save the image
            file = open(fullpath, "wb")
            file.write(response.content)
            #check similarty
            simPercent = similarityPercentage(fullpath)
            #if match is less than number delete it
            if simPercent < 0:
                os.remove(fullpath)
            else:
                break
            
    