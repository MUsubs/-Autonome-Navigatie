import cv2
import time
import scipy.ndimage
import scipy
import os

# Function draw bounding box
def drawBbox(image, bbox):
    # Extracting coordinates and dimensions from bbox
    x, y, w, h = [int(i) for i in bbox]
    # Drawing rectangle around the object being tracked
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Function to process the video
def processVideoinformation(video_path, output_dir):
    # Open file to store information
    informatiefile = open("info_OOZC2.json", "a")  #Name infofile
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    

    # Read the first frame
    ret, frame = cap.read()
    
    # Check if the frame was successfully read
    if not ret:
         raise ValueError("Cannot read video file") 
    
    # Resize the first frame to resolution
    frame = cv2.resize(frame, (640, 480))

    # Selecting ROI (Region of Interest) for tracking
    bbox = cv2.selectROI("Select Object to Track", frame, False)
    # Creating CSRT tracker
    tracker = cv2.TrackerCSRT_create()
    # Initialize the tracker with the selected ROI
    tracker.init(frame, bbox)
    
    # Initialize frame counter and start time for process
    frameCounter = 0
    startTime = time.time()
    
    fps = 30
    delay = int(1000/fps)

    # Loop through each frame of the video
    while True:
         # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break 
        
        # Resize frame to a resolution 
        frame = cv2.resize(frame, (640, 480))

        # Calculate elapsed time
        elapsedTime = time.time() - startTime
        
        # Process frames once per second
        # Update the tracker with the current frame
        if elapsedTime >= 1:
            # Save frames
            frame_filename = os.path.join(output_dir, f"frame_{frameCounter}OOZC2.jpg") #Name frame
            cv2.imwrite(frame_filename, frame)
            
            # Update start time and frame counter
            startTime = time.time()
            # Write bounding box information to file: (frame(nummer), x,y,w,h)
            bboxStr = f"Frame: {frameCounter}, x: {bbox[0]}, y: {bbox[1]}, w: {bbox[2]}, h: {bbox[3]}"
            informatiefile.write(bboxStr + "\n")
            informatiefile.flush()
            
            frameCounter += 1  # Move frameCounter increment here
            
        ret, bbox = tracker.update(frame)
        # Check if tracking is successful
        if ret:
            # Draw bounding box if valid
            x, y, w, h = [int(v) for v in bbox]
            if 0 <= x <= frame.shape[1] and 0 <= y <= frame.shape[0] and w > 0 and h > 0:
                drawBbox(frame, bbox)
        
        # Display the frame with bounding box
        cv2.imshow('Tracking', frame)
        
        # Check for key press
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('r'):
            # Allow user to reselect ROI
            bbox = cv2.selectROI("Select Object to Track", frame, False)
            tracker = cv2.TrackerCSRT_create()
            tracker.init(frame, bbox)

        # Exit the loop if ESC key is pressed
        if key == 27:
            break

    informatiefile.close()
    # Release the video capture
    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    # Video file
    video_path = "make_dataset/data_video/OOZC2.mp4" #path Data video
    #Folder voor frames
    output_dir = "make_dataset/frames"
    # Call the function to process the video
    processVideoinformation(video_path, output_dir)

# Entry point of the script
if __name__ == "__main__":
    main()