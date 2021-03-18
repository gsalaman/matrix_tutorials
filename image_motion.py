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
icon_size = 40

icon_image = Image.open("ghost.jpg")
icon_image = icon_image.resize((icon_size,icon_size))

blank_image = Image.new("RGB", (icon_size, icon_size) )

icon_x = total_columns
icon_y = random.randint(0,total_columns-icon_size)

try:
  print("Press CTRL-C to stop")
  while True:

    # erase old image
    matrix.SetImage(blank_image, icon_x, icon_y)
    
    # update our image location 
    icon_x = icon_x - 1
    if (icon_x < (0 - icon_size)):
      icon_x = total_columns
      icon_y = random.randint(0,total_columns-icon_size)

    # show the image 
    matrix.SetImage(icon_image,icon_x,icon_y)

    sleep(.1)

except KeyboardInterrupt:
  exit(0)

