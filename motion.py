from gamepad_wrapper import Gamepad_wrapper
import time
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
options.gpio_slowdown = 3
matrix = RGBMatrix(options = options)

red = (255,0,0)
blue = (0,0,255)
###########################
# Main
###########################
wait_image = Image.new("RGB",(total_rows,total_columns))
wait_draw = ImageDraw.Draw(wait_image)
wait_draw.text((0,0),"Wait for")
wait_draw.text((0,10),"connect") 
matrix.SetImage(wait_image,0,0)


wrapper = Gamepad_wrapper(1)
while wrapper.player_count() != 1:
  pass
  
blank_image = Image.new("RGB", (total_rows,total_columns))
matrix.SetImage(blank_image,0,0)

curr_x = 32
curr_y = 32
direction = "down"
last_update_time = datetime.now()

player_size = 8

player_image = Image.new("RGB",(player_size,player_size))
player_draw = ImageDraw.Draw(player_image)
player_draw.rectangle((1,1,6,6),fill=blue)
player_draw.rectangle((0,0,2,2),fill=red)
player_draw.rectangle((0,5,2,7),fill=red)
player_draw.rectangle((5,0,7,2),fill=red)
player_draw.rectangle((5,5,7,7),fill=red)

min_delay = .1

while True:
  
  input = wrapper.get_next_input()
  if (input != None):
    direction = input[1]
 
  current_time = datetime.now()
  deltaT = current_time - last_update_time

  if (deltaT.total_seconds() < min_delay):
    time.sleep(0.001)
    continue

  last_update_time = current_time

  # erase the screen 
  matrix.SetImage(blank_image,0,0)

  # figure out where the new player location should be based on direction
  if (direction == "up"):
    if (curr_y > 0):
      curr_y = curr_y - 1
  if (direction == "down"):
    if (curr_y < total_rows - player_size):
      curr_y = curr_y + 1
  if (direction == "left"):
    if (curr_x > 0):
      curr_x = curr_x - 1
  if (direction == "right"):
    if (curr_x < total_columns - player_size):
      curr_x = curr_x + 1

  # draw the new player 
  matrix.SetImage(player_image,curr_x,curr_y)
  
    
