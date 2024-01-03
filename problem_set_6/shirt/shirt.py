from PIL import Image
from PIL.ExifTags import TAGS
import os
import re
import sys
from PIL import Image

def main():
    if valid_args() and valid_ext() and exts_match():
        im_overlay()
        
def valid_args():
    if len(sys.argv) < 3:
        print("Too few command line arguments")
        exit(1)
    elif len(sys.argv) > 3:
        print("Too many command line arguments")
        exit(1)
    
    return True
    
def valid_ext():
    input_file = sys.argv[1].strip().lower()
    output_file = sys.argv[2].strip().lower()
    if not re.match(r'.*\.(jpg|jpeg|png)$', input_file and output_file):
        print("Invalid input")
        exit(1)
    
    return True     

def exts_match():
    if not os.path.splitext(sys.argv[1])[1] == os.path.splitext(sys.argv[2])[1]:
        print("Input and output have different extensions")
        exit(1)
    
    return True

def im_overlay():
    im_overlay = Image.open("shirt.png")
    im_before = Image.open(sys.argv[1])
    im_height, im_width = im_before.size # Split tuple into two variables
    im_overlay = im_overlay.resize((im_height, im_width))
    position = (0, -100)
    im_before.paste(im_overlay, position, mask=im_overlay)
    im_before.show()
    im_before.save(sys.argv[2])

if __name__ == "__main__":
    main()
    