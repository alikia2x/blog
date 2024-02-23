from PIL import Image
import os

def convert_to_progressive(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        # Get the full path of the file
        input_path = os.path.join(input_folder, file_name)

        # Determine the output format based on the original format
        output_format = "JPEG" if file_name.lower().endswith(('.jpg', '.jpeg')) else "PNG"

        # Create the output path with the "progressive" suffix and original file extension
        base_name, ext = os.path.splitext(file_name)
        output_path = os.path.join(output_folder, f"{base_name}{ext.lower()}")

        try:
            # Open the image and save it in progressive format
            img = Image.open(input_path)
            img.save(output_path, format=output_format, progressive=True)
            print(f"Converted {file_name} to progressive {output_format}")
        except Exception as e:
            print(f"Error converting {file_name}: {e}")

if __name__ == "__main__":
    input_folder = "./static/img-o/"
    output_folder = "./static/img/"

    convert_to_progressive(input_folder, output_folder)
