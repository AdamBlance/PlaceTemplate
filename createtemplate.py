# amogus

import argparse
import sys
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument(
    'input_image', metavar='input-image', type=Path,
    help='image to turn into a template')
parser.add_argument(
    'output_image', metavar='output-image', type=Path,
    help='output template file'
)

args = parser.parse_args()

if not args.input_image.is_file():
    sys.exit('Image path does not point to a file')

with Image.open(args.input_image) as im:
    pixels = im.load()

# Get input image dimensions
width, height = im.size

# Create blank image in memory with 3x the size
output = Image.new('RGBA', (width*3, height*3), color=(0,0,0,0))

# Place input pixels in the middle of transparency in output image
# T T T
# T X T
# T T T
for y in range(height):
    for x in range(width):
        output.putpixel((1+(x*3), 1+(y*3)), pixels[x,y])

output.save(args.output_image)
