import cv2
import time
import scipy.ndimage
import scipy

# Function draw bounding box
def drawBbox(image, bbox):
    # Extracting coordinates and dimensions from bbox
    x, y, w, h = [int(i) for i in bbox]
    # Drawing rectangle around the object being tracked
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Function to process the video
def processVideoinformation(video_path):
    # Open file to store information
    informatiefile = open("informatie(zwembad1).json", "a")
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    

    # Read the first frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(frame, (9,9), sigmaX=0, sigmaY=0)
    mask1 = [[0.5, 1, 0.5], [  1,-6,   1], [0.5, 1, 0.5]]
    edge_detect4 = scipy.ndimage.convolve(img_blur, mask1)
    img_blur2 = cv2.blur(edge_detect4, (3,3))
    img_smooth = cv2.medianBlur(img_blur2, 3)
    frame = img_smooth
    
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
    
    # Loop through each frame of the video
    while True:
         # Read the next frame
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.GaussianBlur(frame, (9,9), sigmaX=0, sigmaY=0)
        mask1 = [[0.5, 1, 0.5], [  1,-6,   1], [0.5, 1, 0.5]]
        edge_detect4 = scipy.ndimage.convolve(img_blur, mask1)
        img_blur2 = cv2.blur(edge_detect4, (3,3))
        img_smooth = cv2.medianBlur(img_blur2, 3)
        frame = img_smooth
        if not ret:
            break 
        
        # Resize frame to a resolution 
        frame = cv2.resize(frame, (640, 480))

        # Calculate elapsed time
        elapsedTime = time.time() - startTime
        
        # Process frames once per second
        # Update the tracker with the current frame
        ret, bbox = tracker.update(frame)
        # Check if tracking is successful
        if ret:
            # Draw bounding box if valid
            x, y, w, h = [int(v) for v in bbox]
            if 0 <= x <= frame.shape[1] and 0 <= y <= frame.shape[0] and w > 0 and h > 0:
                drawBbox(frame, bbox)
        if elapsedTime >= 1:
            # Save frames
            cv2.imwrite(f"frame{frameCounter}(zwembad1).jpg", frame)
            # Update start time and frame counter
            startTime = time.time()
            # Write bounding box information to file: (frame(nummer), x,y,w,h)
            bboxStr = f"Frame: {frameCounter}, x: {bbox[0]}, y: {bbox[1]}, w: {bbox[2]}, h: {bbox[3]}"
            informatiefile.write(bboxStr + "\n")
            informatiefile.flush()
            
            frameCounter += 1  # Move frameCounter increment here
            
       # else:
            # Log tracker failure
            #print(f"Tracking failed at frame {frameCounter}")
            #informatiefile.write(f"Tracking failed at frame {frameCounter}\n")
            #informatiefile.flush()
        
        # Display the frame with bounding box
        cv2.imshow('Tracking', frame)
        
        # Check for key press
        key = cv2.waitKey(1) & 0xFF
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
    video_path = "zwembad1.MP4"
        # Call the function to process the video
    processVideoinformation(video_path)

# Entry point of the script
if __name__ == "__main__":
    main()
