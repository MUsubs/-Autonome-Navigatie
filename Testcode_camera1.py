import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('CameraView 1 Voorkant', frame)
    edge_detect = cv2.Canny(frame, 100, 200)
    cv2.imshow('Edge detect camera 1', edge_detect)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
