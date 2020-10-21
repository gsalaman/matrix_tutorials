
# Used in main loop
from time import sleep
from datetime import datetime

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

matrix = RGBMatrix(options = options)

###################################
# Main loop 
###################################
last_update_time = datetime.now()

image = Image.new("RGB", (1,1))
draw = ImageDraw.Draw(image)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
draw.rectangle((0,0,0,0),outline=red, fill=red)

blank_image = Image.new("RGB", (1,1))
blank_draw = ImageDraw.Draw(blank_image)
blank_draw.rectangle((0,0,0,0),outline=(0,0,0),fill=(0,0,0)

for minute in range (5):
  for second in range (60):
    matrix.SetImage(image,second,minute*5)
    time.sleep(1)
    matrix.SetImage(blank_image, second, minute * 5)

