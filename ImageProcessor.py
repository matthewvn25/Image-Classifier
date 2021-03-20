# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageChops
from numpy import asarray

#"pip install praw" in console to install praw
import praw
import urllib
import requests
import os.path
import time

import sys
import os, numpy

#from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

def main():
    #uncomment below if you want to scrape
    webScrape(10)
    
    if os.path.exists("TestSet"): #more for the download
        #createCentroidsHelper()
        testImageNames = os.listdir("TestSet")
        for name in testImageNames:
            if(name != ".DS_Store"):
                #print(name)
                similarityPercentage(name,Image.open("TestSet/" + name))
                print()
    else:
        print("TestSet file does not exist. Ending program.")
        

def webScrape(n):
    """Web scrapes the subreddit "AnimeWallpaper" for n images.
    
    :param n : the number of images the web scraper will keep.
    """
    print("Beginning Web Scrape for " + str(n) + " images. Omachi kudasai.")
    
    if(not(os.path.exists("TestSet"))):
        os.mkdir("TestSet")
        
    #Login infor to use Praw in reddit. Created and registered an app in reddit
    reddit = praw.Reddit(client_id = '6oQuWT8j5mrj0g',
                         client_secret = 'lwCsLOu6b9Doayj96CHyuCWJo0fVtg',
                         user_agent = 'GeminiScraper')
    
    folder = 'TestSet/'
    #Generates a list of posts on the subreddit that can be navigated
    #though one at a time
 
    postsListGenerator = reddit.subreddit("AnimeWallpaper").new(limit=n)
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
# =============================================================================
#             simPercent = similarityPercentage(fullpath)
#             #if match is less than number delete it
#             if simPercent < 0:
#                 os.remove(fullpath)
#             else:
#                 break
# =============================================================================
    
def similarityPercentage(sourceName,source):
    """Prints the similarity percentages between source image and centroids
    The source image and centroids are transformed into the same resolution.
    The absolute difference between the source image and each centroid is taken.
    The absolute difference, an Image object, is iterated through pixel by pixel to calculate the similarity between each pixel.
    
    :param source : source image to compare centroids to
    """
    
    dict = {}
    names = os.listdir("Centroids")
    centroids = []
    for name in names:
        centroids.append(Image.open("Centroids/" + name))
        
    #https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html
    
    if(not(os.path.exists("Waifus"))):
        os.mkdir("Waifus")
        
    for k in range (len(centroids)):
        smallestRes = findSmallerResolution(source, centroids[k])
        source = source.resize(smallestRes, Image.ANTIALIAS)
        centroids[k] = centroids[k].resize(smallestRes, Image.ANTIALIAS)
        
        source_pixels = source.load()
        centroid_pixels = centroids[k].load()
        
        #obtain absolute difference of 2 images
        try:
            absDiff = ImageChops.difference(source, centroids[k])
            absDiff_pixels = absDiff.load()
            
            similarPixelCount = 0
            for i in range (smallestRes[0]): 
                for j in range(smallestRes[1]):
                    #The pixel absolute distance of 100 was chosen arbitrarily. Subject to change.
                    if(absDiff_pixels[i,j][0] + absDiff_pixels[i,j][1] + absDiff_pixels[i,j][2] <= 100):
                         similarPixelCount =  similarPixelCount + 1
                         
            dict[names[k]] = round(similarPixelCount / (smallestRes[0] * smallestRes[1]) * 100, 3) 
            
        except ValueError:
            print(sourceName + " has been moved to ValueError folder because image type not match with centroid (ValueError).")
            if(not(os.path.exists("Waifus/ValueError"))):
                try:
                    os.mkdir("Waifus/ValueError")
                except OSError as error: 
                    print('OSError')
                try:
                    os.replace("TestSet/"+sourceName, "Waifus/ValueError/"+sourceName) 
                except FileNotFoundError as fne:
                    print(sourceName + " not found.")
            return #no need to get highest key if image is ValueError
        
        
    #create variables for best images from dict
    highest = 0
    highestKey = ""
    #save the highest percent and key
    print(sourceName + "\t")
    for key in dict:
        print("\t" + key + ": " + str(dict[key]) + "%")
        if dict[key] > highest:
            highest = dict[key]
            highestKey = key
    #replace the name so that it can match the folder
    highestKey = highestKey.replace('centroid_',''). \
        replace('.png','')
        
    #print(highest)
    #print(highestKey)
    
    #creates directory for each centroid if it does not exist
    for folderNames in os.listdir("LearningSets"):
        if(not(os.path.exists("Waifus/"+folderNames))):
            try:
                os.mkdir("Waifus/"+folderNames)
            except OSError as error: 
                print('OSError')
                
    #Takes the image from the test set and moves to the proper folder
    #can use os.rename instead
    #Currently moves all images to highest percent but does not give overall highest
    
    #Check for FileNotFoundError
    try:
        os.replace("TestSet/"+sourceName, "Waifus/"+highestKey+"/"+sourceName)  
    except FileNotFoundError as fnf:
        print(sourceName + " will remain in TestSet because of FileNotFoundError.")
        
        
def findSmallestResolution(imageList):
    """Returns the smallest resolution from a List of Image Objects.
    Each resolution is calculated by multiplying the Image Object's length and width
    
    :param imageList : a List of Image Objects
    :return smallestRes : the smallest resolution as a tuple
    """
    
    numOfImages = len(imageList)
    if(numOfImages <= 0):
        return (0,0)
    else:
        smallestRes = imageList[0].size
        for i in range (1, numOfImages):
            if(smallestRes[0] * smallestRes[1] > imageList[i].size[0] * imageList[i].size[1]):
                smallestRes = imageList[i].size
        return smallestRes
    
def findSmallerResolution(img1, img2):
    """Returns the smallest resolution of 2 Image Objects
    Each resolution is calculated by multiplying the Image Object's length and width
    
    :param img1 : first image
    :param img2 : second image
    :return smallestRes : the smallest resolution as a tuple
    """
    
    smallestRes = img1.size
    if(img1.size[0] * img1.size[1] > img2.size[0] * img2.size[1]):
        smallestRes = img2.size
    return smallestRes
    
def createCentroidsHelper():
    """Does preparation work before creating centroids
    """
    
    categories = os.listdir("LearningSets")
    for category in categories:
        imageNames = os.listdir("LearningSets/" + category)
        imageList = []
        for image in imageNames:
            imageList.append(Image.open("LearningSets/" + category + "/" + image))
            
        centroid = createCentroid(imageList, findSmallestResolution(imageList))
        #centroid.show()
        centroid.save("Centroids/centroid_" + category + ".png", "PNG")  
        
def createCentroid(imageList, smallestRes):
    """Returns the centroid (average image) from a List of Image Objects.
    
    :param imageList : a List of Image Objects
    :param smallestRes : the smallest resolution in imageList
    :return out : the average of all images in imageList as the size of smallestRes
    """
    
    N = len(imageList)
    #create float array to hold pixel values
    arr = numpy.zeros((smallestRes[1], smallestRes[0], 3), numpy.float)
    
    for image in imageList:
        resized = image.resize(smallestRes, Image.ANTIALIAS)
        #convert resized image into float array
        imarr = numpy.array(resized, dtype = numpy.float)
        arr = arr + imarr/N
                
    #convert and round float array to int
    arr = numpy.array(numpy.round(arr), dtype = numpy.uint8)
    out = Image.fromarray(arr, mode = "RGB")
    return out

main()