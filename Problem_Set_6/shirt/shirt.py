import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if the number of arguments is exactly 3 (script name + 2 arguments)
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image> <output_image>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the input and output files have valid extensions
    valid_extensions = ['.jpg', '.jpeg', '.png']
    input_ext = os.path.splitext(input_filename)[1].lower()
    output_ext = os.path.splitext(output_filename)[1].lower()

    if input_ext not in valid_extensions:
        print("Invalid input format")
        sys.exit(1)

    if output_ext not in valid_extensions:
        print("Invalid output format")
        sys.exit(1)

    # Check if input and output files have the same extension
    if input_ext != output_ext:
        print("Input and output have different extensions")
        sys.exit(1)

    # Check if the input file exists
    if not os.path.isfile(input_filename):
        print("Input does not exist")
        sys.exit(1)

    try:
        # Open the input image and the shirt image
        input_image = Image.open(input_filename)
        shirt = Image.open("shirt.png")

        # Debugging information
        print(f"Input image size: {input_image.size}")
        print(f"Shirt image size: {shirt.size}")

        # Get the size of the shirt image
        shirt_size = shirt.size

        # Resize and crop the input image to match the size of the shirt
        input_image = ImageOps.fit(input_image, shirt_size)

        # Overlay the shirt on the input image
        input_image.paste(shirt, shirt)

        # Save the resulting image to the output file
        input_image.save(output_filename)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
