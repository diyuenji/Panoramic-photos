# import the necessary packages
from panorama import Stitcher
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
def connect_two_images(imageA,imageB):

    # load the two images and resize them to have a width of 400 pixels
    # (for faster processing)
    # imageA = cv2.imread(args["first"])
    # imageB = cv2.imread(args["second"])
    imageA = imutils.resize(imageA, height=400)
    imageB = imutils.resize(imageB, height=400)
    # print(imageA.shape)
 
    # print(imageB.shape)
    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    # show the images
    # cv2.imshow("Image A", imageA)
    # cv2.imshow("Image B", imageB)
    cv2.imshow("Keypoint Matches", vis)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    return result



ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
    help="path to the first image")
ap.add_argument("-s", "--second", required=True,
    help="path to the second image")
ap.add_argument("-t", "--third", required=True,
    help="path to the third image")
args = vars(ap.parse_args())


imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageC = cv2.imread(args["third"])
imageAB=connect_two_images(imageA,imageB)
results=connect_two_images(imageAB,imageC)
cv2.imwrite("result.jpg", results)
# run code python stitch.py --first left.png --second middle.png --third right.png
# python stitch.py --first Left1.jpg --second Middle1.jpg --third Right1.jpg