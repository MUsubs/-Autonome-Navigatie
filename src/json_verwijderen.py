import os

def removeJSONfiles():
    # Get the current directory
    currentDirectory = os.getcwd()
    
    # List all files in the current directory
    files = os.listdir(currentDirectory)
    
    # Filter out JSON files
    json_files = [file for file in files if file.endswith('.json')]
    
    # Remove each JSON file
    for json_file in json_files:
        filePath = os.path.join(currentDirectory, json_file)
        try:
            os.remove(filePath)
            print(f"Removed {filePath}")
        except Exception as e:
            print(f"Error removing {filePath}: {e}")

if __name__ == "__main__":
    removeJSONfiles()
