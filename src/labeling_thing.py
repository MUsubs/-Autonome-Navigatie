def copyInfo(informatieFilePath):
    # Open the informatiefile for reading
    with open(informatieFilePath, "r") as informatieFile:
        # Loop through each line in the informatiefile
        for line in informatieFile:
            # Extract frame number from the line
            frameNumber = line.split(",")[0].split(":")[1].strip()
            # Define the filename for this frame
            frameFileName = f"frame{frameNumber}(**NAAM**).json"
            # Write the line to the corresponding file without the frame number
            with open(frameFileName, "w") as frameFile:
                # Extract the text part without the frame number
                textPart = ",".join(line.split(",")[1:]).strip()
                frameFile.write(textPart)

# Entry point of the script


if __name__ == "__main__":
    # Path to the informatiefile
    informatieFilePath = "informatie().json"
    # Call the function to copy informatiefile content to individual frame files
    copyInfo(informatieFilePath)
