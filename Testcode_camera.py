import cv2
import numpy as np

#This function contains a blocking while loop
def cameraView(cameranr):
        cap = cv2.VideoCapture(1)
        
        while (cap.isOpened()):
            frame = cap.read()
            frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

            if cameranr == 1:
                cv2.imshow('CameraView 1 Voorkant', frame)
                edge_detect = cv2.Canny(frame, 100, 200)
                cv2.imshow('Edge detect camera 1', edge_detect)
            elif cameranr == 2:
                cv2.imshow('Cameraview 2 Bovenview', frame)
                edge_detect = cv2.Canny(frame, 100, 200)
                cv2.imshow('Edge detect camera 2', edge_detect)
            elif cameranr == 3:
                cv2.imshow('Cameraview 3 zijkant', frame)
                edge_detect = cv2.Canny(frame, 100, 200)
                cv2.imshow('Edge detect camera 3', edge_detect)
            else:
                print("Wrong Cameranumber.")

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

def main():
     cameraView(1)

if __name__ == "__main__":
	main()