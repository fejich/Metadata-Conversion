from PIL import Image
import os

def convert_jpg_to_png():
    """
    Convert all JPG files in the current directory to PNG format.
    Output files will have the same name but with .png extension.
    """
    # Get current working directory
    directory = os.getcwd()
    
    # Process each file in current directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(directory, filename)
            try:
                # Open the JPG image
                img = Image.open(input_path)
                
                # Create output path with same name but .png extension
                output_path = os.path.splitext(input_path)[0] + '.png'
                
                # Save as PNG
                img.save(output_path, 'PNG')
                print(f"Successfully converted {filename} to {os.path.basename(output_path)}")
                
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ == "__main__":
    convert_jpg_to_png()