from PIL import Image
from PIL.ExifTags import TAGS
import os
import re
import sys
from PIL import Image

def main():
    image = Image.open("muppet.jpg")
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

    image_height, image_width = image.size

if __name__ == "__main__":
    main() 