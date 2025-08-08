import re
import os

def parse_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split into game entries
    games = content.split('\ngame: ')[1:]  # Skip the initial collection metadata
    
    # Extract file names
    file_names = []
    for game in games:
        file_match = re.search(r'file: (.*?)\n', game)
        if file_match:
            file_names.append(file_match.group(1))
    
    return file_names

def create_files(file_names, output_dir):
    # Create empty files in the specified directory
    for file_name in file_names:
        file_path = os.path.join(output_dir, file_name)
        # Ensure the directory structure exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # Create empty file
        with open(file_path, 'w') as f:
            pass
        print(f"Created file: {file_path}")

def main():
    metadata_file = "metadata.pegasus.txt"
    try:
        # Get the directory of the metadata file
        output_dir = os.path.dirname(os.path.abspath(metadata_file))
        file_names = parse_metadata(metadata_file)
        create_files(file_names, output_dir)
        print(f"Successfully created {len(file_names)} files in {output_dir}")
    except FileNotFoundError:
        print(f"Error: {metadata_file} not found")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()