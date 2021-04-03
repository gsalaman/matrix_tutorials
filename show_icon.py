from time import sleep
import datetime

import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# this is the size of ONE of our matrixes. 
matrix_rows = 64 
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'regular'
options.gpio_slowdown = 3
 
matrix = RGBMatrix(options = options)

###################################
# Main code 
###################################
icon_size = 16

icon_image = Image.open("minesweeper_flag.png")
icon_image = icon_image.convert("RGB")

# don't need this, as we're already 16x16
#icon_image = icon_image.resize((icon_size,icon_size))

icon_x = 16 
icon_y = 16 

try:
  print("Press CTRL-C to stop")
  while True:

    # show the image 
    matrix.SetImage(icon_image,icon_x,icon_y)

    sleep(.1)

except KeyboardInterrupt:
  exit(0)

