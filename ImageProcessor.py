# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageChops
from numpy import asarray

import sys

#from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
# =============================================================================
# im2 = Image.open("Images\Image2.png")
# im3 = Image.open("Images\Image3.png")
# 
# diff = ImageChops.difference(im2, im3)
# 
# print('new line')
# print(diff)
# 
# diff.save("Output/out.jpg", "JPEG")
# =============================================================================

def main():
    print("hello")
    #testDict()
    #testPixelChange()
    source = Image.open("Images\Image6.png")
    #mostSimilar(source)
    similarityPercentage(source)

def testPixelChange():
    im2 = Image.open("Images\Image2.png")
    
    pixels = im2.load() # crate the pixel map
    z = 0
    for i in range (im2.size[0]):
        for j in range(im2.size[1]):
            z = z + 1
            #pixels[i,j] = (i, j, 100) #set color
            #print(pixels[i,j][0])
            
    im2.save("Output/im2.jpg", "JPEG")

def mostSimilar(source):

    source_pixels = source.load()
    dict = {}
    for k in range (7): #for each image in the folder
        imgName = "Image" + str(k) + ".png"
        img = Image.open("Images\\" + imgName)
        img_pixels = img.load()
        totalDiff = 0
        for i in range (source.size[0]): # for each row in the image
            for j in range(source.size[1]): # for each col in the image
                totalDiff = totalDiff + abs(source_pixels[i,j][0] - img_pixels[i,j][0]) + \
                    abs(source_pixels[i,j][1] - img_pixels[i,j][1]) + \
                    abs(source_pixels[i,j][2] - img_pixels[i,j][2])
        dict[imgName] = totalDiff
        #dict[imgName] = totalDiff / (source.size[0] * source.size[1])
    for key in dict:
        print(key + ": " + str(dict[key]))
    
#research eigen values
def similarityPercentage(source):
    similarityPercentage = {}
    for k in range (7): #for each image in the folder
        imageName = "Image" + str(k) + ".png"
        img = Image.open("Images\\" + imageName)
        absDiff = ImageChops.difference(source, img)
        absDiff_pixel = absDiff.load()
        zeroCount = 0
        
        for i in range (absDiff.size[0]): # for each row in the image
            for j in range(absDiff.size[1]): # for each col in the image
                if(absDiff_pixel[i,j] == (0,0,0)):
                    zeroCount = zeroCount + 1
        similarityPercentage[imageName] = zeroCount * 100 / (absDiff.size[0] * absDiff.size[1])
        
    for key in similarityPercentage:
        print(key + ": " + str(similarityPercentage[key]) + "%")
                
def testDict():
    dict = {"key" : 2, "sick" : 66}
    dict ["new key"] = 55
    print(dict)
            #pixels[i,j] = (i, j, 100) #set color
main()
