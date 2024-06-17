import cv2
import numpy as np
import scipy.ndimage
from skimage import data, filters, feature
from skvideo import io
import scipy
from scipy import ndimage
import skvideo


cap = cv2.VideoCapture("C:/Users/slden/TI_software/R2D2/Autonome-Navigatie/Voorkant_VID6.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    if (ret == True):
        frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Cameraview 2 Bovenview', frame)
        img_blur = cv2.GaussianBlur(frame, (9,9), sigmaX=0, sigmaY=0)
        mask1 = [[0.5, 1, 0.5], [  1,-6,   1], [0.5, 1, 0.5]]
        edge_detect4 = scipy.ndimage.convolve(img_blur, mask1)
        img_blur2 = cv2.blur(edge_detect4, (3,3))
        img_smooth = cv2.medianBlur(img_blur2, 3)
        cv2.imshow('Laplacian, gaussian blur 9x9', img_smooth)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
        
        
        
        # img_blur2 = cv2.GaussianBlur(frame, (3,3), sigmaX=0, sigmaY=0)
        # edge_detect = cv2.Canny(frame, 100, 200)
        # edge_detect2 = cv2.Sobel(src=img_blur2, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
        # img_blur3 = cv2.GaussianBlur(frame, (13,13), sigmaX=0, sigmaY=0)
        # img_blur4 = cv2.GaussianBlur(frame, (3,3), sigmaX=0, sigmaY=0)
        # edge_detect3 = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
        # edge_detect5 = scipy.ndimage.convolve(img_blur2, mask1)
        # edge_detect5 = scipy.ndimage.convolve(img_blur3, mask1)
        # edge_detect6 = scipy.ndimage.convolve(img_blur4, mask1)
        # cv2.imshow('Laplacian, gaussian blur 9x9x2', edge_detect5)
        # cv2.imshow('canny', edge_detect)
        # cv2.imshow('3', edge_detect2)
        # cv2.imshow('9', edge_detect3)