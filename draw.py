# Used in main loop
from time import sleep

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

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
options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# white rectangle around the whole screen
draw.rectangle( (0,0,total_columns-1,total_rows-1), outline = (255,255,255) )

# a few diagonal lines.  Note in the last we can define points off screen.
draw.line((0,0,32,96),fill=red)
draw.line((5,0,37,96),fill=green)
draw.line((10,-10,42,96),fill=blue)

# a circle is a special ellipse
draw.ellipse((32,32,48,48),fill=None, outline=blue)

# text
draw.text((20,0),"Hello")

matrix.SetImage(image, 0, 0)

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

