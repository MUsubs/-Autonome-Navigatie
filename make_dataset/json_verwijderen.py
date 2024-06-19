import os

def removeJsonFiles():
    """
    Removes all JSON files in current directory.
    """
    # Get the current directory
    current_directory = "make_dataset/frames" # path for json files to deleted
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    
    # Filter out JSON files
    json_files = [file for file in files if file.endswith('.json')]
    
    # Remove each JSON file
    for json_file in json_files:
        file_path = os.path.join(current_directory, json_file)
        try:
            os.remove(file_path)
            print(f"Removed {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")

if __name__ == "__main__":
    removeJsonFiles()
