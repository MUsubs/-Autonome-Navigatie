import os

def copyInfo(informatieFilePath, output_dir):
    # Open the informatiefile for reading
    with open(informatieFilePath, "r") as informatieFile:
        # Loop through each line in the informatiefile
        for line in informatieFile:
            # Extract frame number from the line
            frameNumber = line.split(",")[0].split(":")[1].strip()
            # Define the filename for this frame
            frameFileName = os.path.join(output_dir, f"frame_{frameNumber}OOZC2.json") #Name frame
            # Write the line to the corresponding file without the frame number
            with open(frameFileName, "w") as frameFile:
                # Extract the text part without the frame number
                textPart = ",".join(line.split(",")[1:]).strip()
                frameFile.write(textPart)

# Entry point of the script


if __name__ == "__main__":
    # Path to the informatiefile
    informatieFilePath = "make_dataset/info_OOZC2.json" # Path infofile
    # Path for saved files
    output_dir = "make_dataset/frames" #Path for new frames
    # Call the function to copy informatiefile content to individual frame files
    copyInfo(informatieFilePath, output_dir)