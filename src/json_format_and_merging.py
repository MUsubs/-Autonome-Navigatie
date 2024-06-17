import os
import json

def mergeJsonContents():
    combined_data = {}

    # Get the list of files in the current directory
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        if filename.endswith('.json'):
            # Read the content of the JSON file
            with open(filename, 'r') as f:
                content = f.read().strip()
            # Split content at commas to get individual key-value pairs
            parts = content.split(',')
            data = {}
            has_data = False
            for part in parts:
                # Split each part by ":" to get key and value
                try:
                    key, value = part.split(':')
                except ValueError:
                    continue  
                key = key.strip()
                value = value.strip()
                data[key] = value
                has_data = True
            # If the JSON file has no data, add only the filename with an empty dictionary
            if not has_data:
                combined_data[filename] = {}

            # Add filename and data to the combined data if it has data
            if has_data:
                combined_data[filename] = data

    return combined_data

def main():
    # Merge the JSON contents
    combined_data = mergeJsonContents()

    # Write the combined data to an output JSON file
    output_file = 'combined.json'
    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=4)

    print(f"Combined JSON content written to {output_file}")

if __name__ == "__main__":
    main()
