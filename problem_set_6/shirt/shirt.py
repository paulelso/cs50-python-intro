from PIL import Image, ImageOps
from PIL.ExifTags import TAGS
import os
import re
import sys

def main():
    if valid_args() and valid_ext() and exts_match():
        im_overlay()
        
def valid_args(): # Check if there are two command line arguments
    if len(sys.argv) < 3:
        print("Too few command line arguments")
        exit(1)
    elif len(sys.argv) > 3:
        print("Too many command line arguments")
        exit(1)
    
    return True
    
def valid_ext(): # Check if input and output files have valid extensions
    input_file = sys.argv[1].strip().lower()
    output_file = sys.argv[2].strip().lower()
    if not re.match(r'.*\.(jpg|jpeg|png)$', input_file and output_file):
        print("Invalid input")
        exit(1)
    
    return True     

def exts_match(): # Check if input and output files have the same extensions
    if not os.path.splitext(sys.argv[1])[1] == os.path.splitext(sys.argv[2])[1]:
        print("Input and output have different extensions")
        exit(1)
    
    return True

def im_overlay(): # Overlay the shirt image onto the input image
    im_overlay = Image.open("shirt.png")
    im_before = Image.open(sys.argv[1])
    im_height, im_width = im_overlay.size # Split tuple into two variables
    # Returns a resized and padded version of the image, cropped to the requested aspect ratio and size.
    im_before = ImageOps.fit(im_before, (im_height, im_width), centering=(0.5, 0.5))
    im_before.paste(im_overlay, mask=im_overlay)
    im_before.save(sys.argv[2])

if __name__ == "__main__":
    main()
    