# Image-Classifier
How to use:
  1. The folders should already be set up upon download but here are notes below:
  2. You should have a folder named "LearningSets" in the same directory of the project. The LearningSets folder will have sub folders of each category you want to classify. By default, we have Autumn, Blossoms, Guitar, and so on. Each sub folder will have images that you personally classify as that particular category.
  3. If we return back to the project directory, you will notice the "Centroids" folder. Centroids are the average image taken from each category. If you would like to create another centroid, you can use the createCentroidsHelper() function to do so. You will first create the desired category in the LearningSets directory and places images (jpeg or png) into the folder.
  4. Run ImageProcessor.py
  5. ImageProcessor.py will download the first n images from https://www.reddit.com/r/Animewallpaper/ . 'N' by default is set to 10 in the webScrape(n) function. These images will be kept in the folder "TestSet". The TestSet folder will be created if it does not exist already.
  6. After all images are downloaded, a folder named "Waifus" will be created with subfolders for each category from the LearningSet. Each image will be compared to each centroid to classify the image. Images are compared pixel by pixel and must be within a pixel absolute distance of 100 units. I chose 100 as a arbitary alue and can be adjusted later on.
  7. There are definitely some bugs that need to be addressed. During the classification phase of the project, some images cannot be compared with the centroids and cause a "ValueError" and some images cause a "FileNotFoundError" even when the image is clearly in its correct directory (I think). So, there are try/except statements to make sure the project does not crash.

There is a GUI currently in development so that is why you see a GUI project. It does not work yet.
The image classification here is mediocre at best. I did some reading and because images are essentially a 2D matrix, we can maybe use some matrix math eventually like the Norm or something.
ImageScraper.py is no longer needed but is kept for reference.
Thank you for reading.
