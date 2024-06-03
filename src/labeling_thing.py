def copyInfo(informatieFilePath):
    # Open the informatiefile for reading
    with open(informatieFilePath, "r") as informatieFile:
        # Loop through each line in the informatiefile
        for line in informatieFile:
            # Extract frame number from the line"
            frameNumber = line.split(",")[0].split(":")[1].strip()
            # Define the filename for this frame
            frameFileName = f"frame{frameNumber}.txt"
            # Write the line to the corresponding file
            with open(frameFileName, "w") as frameFile:
                frameFile.write(line)

# Entry point of the script
if __name__ == "__main__":
    # Path to the informatiefile
    informatieFilePath = "informatie.txt"
    # Call the function to copy informatiefile content to individual frame files
    copyInfo(informatieFilePath)
