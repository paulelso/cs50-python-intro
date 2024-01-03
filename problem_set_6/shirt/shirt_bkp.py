from PIL import Image
from PIL.ExifTags import TAGS
import os
import re
import sys
from PIL import Image


def main():
    im_overlay = Image.open("shirt.png")
    im_before = Image.open("before3.jpg")
    im_height, im_width = im_before.size # Split tuple into two variables
    im_overlay = im_overlay.resize((im_height, im_width))
    position = (0, -100)
    im_before.paste(im_overlay, position, mask=im_overlay)
    im_before.show()
    im_before.save("after3.jpg")

    

    """
    shirt_im.size(before_im.size)
    before_im.paste(shirt_im, (0,0))
    shirt_im.show()



    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    for label,value in info_dict.items():
        print(f"{label:25}: {value}")


      
    if valid_args() and valid_ext() and exts_match():
        shirt = Image.open(sys.argv[1])
        size = (400, 400)
        photo = Image.new('RGB', size)
        photo.paste(shirt, size)
        exit(0)
    """
        
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

if __name__ == "__main__":
    main()
    