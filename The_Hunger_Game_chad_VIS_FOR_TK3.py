'''Missionaries3_VIS_FOR_TK3.py
Version of Sept. 17, 2019.
This visualization file works with Missionaries3.py and
Tk_SOLUZION_Client3.py.
It uses three jpg images for showing missionaries, cannibals, and the boat.

'''
from tkinter import font
import os
# from The_Hunger_Game_text import *
import redraw

myFont=None

WIDTH = int(2732*0.2)-7
HEIGHT = int(2048*0.2)-1
TITLE = 'The Hunger Game'

STATE_WINDOW = None
STATE_ARRAY = None
ROOT = None
THE_CANVAS = None

def initialize_vis(st_win, state_arr, initial_state):
  global STATE_WINDOW, STATE_ARRAY, ROOT, THE_CANVAS, WIDTH, HEIGHT
  # State.holdwindow = ROOT
  STATE_WINDOW = st_win
  STATE_ARRAY = state_arr
  STATE_WINDOW.winfo_toplevel().title(TITLE)
  # r = redraw.Redraw(STATE_WINDOW.master, WIDTH, HEIGHT)
  render_state(initial_state)

def give_canvas(canvas, window):
  r = redraw.Redraw(canvas, WIDTH, HEIGHT, window)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=8)
    #print("In render_state, state is "+str(s))
    # Create the default array of colors

    green = (62, 137, 20)
    blue = (3, 94, 123)
    
    red = (244, 68, 46)
    orange = (248, 102, 36)
    yellow = (234, 196, 53)
    
    row = [blue]* 11
    the_color_array = [row, row[:], row[:], row[:], row[:], row[:], row[:], row[:]]
    
    # Now create the default array of string labels.
    row = ['' for i in range(11)]
    the_string_array = [row, row[:], row[:], row[:], row[:], row[:], row[:], row[:]]


    #side hunger bar
    the_string_array[3][0] = f"Hunger:\n\n{s.h:.2f}%"

    # Adjust colors and strings to match the state.
    the_string_array[0][1] = f"{s.time + 2022}  "

    the_string_array[0][2] = "$" + str(s.m) + " "

    for i in range(88):
      if os.name == "posix":
        the_color_array[int(i/11)][i%11] = f"mapimagesv2/mapslicev2_{i+1:02}.jpg"
      else:
        the_color_array[int(i/11)][i%11] = f"mapimagesv2\mapslicev2_{i+1:02}.jpg"

    if s.crisis is not None:
      if os.name == "posix":
        the_color_array[0][10] = f"mapimagesv2/crisis_active_02.jpg"
      else:
        the_color_array[0][10] = f"mapimagesv2\crisis_active_02.jpg"

    if s.h >= 25:
      if os.name == "posix":
        the_color_array[6][0] = f"mapimagesv2/hunglvl1_67.jpg"
        the_color_array[5][0] = f"mapimagesv2/hunglvl1_56.jpg"
      else:
        the_color_array[6][0] = f"mapimagesv2\hunglvl1_67.jpg"
        the_color_array[5][0] = f"mapimagesv2\hunglvl1_56.jpg"

    if s.h >= 40:
      if os.name == "posix":
        the_color_array[6][0] = f"mapimagesv2/hunglvl2_67.jpg"
        the_color_array[5][0] = f"mapimagesv2/hunglvl2_56.jpg"
      else:
        the_color_array[6][0] = f"mapimagesv2\hunglvl2_67.jpg"
        the_color_array[5][0] = f"mapimagesv2\hunglvl2_56.jpg"

    if s.h >= 55:
      if os.name == "posix":
        the_color_array[6][0] = f"mapimagesv2/hunglvl3_67.jpg"
        the_color_array[5][0] = f"mapimagesv2/hunglvl3_56.jpg"
        the_color_array[4][0] = f"mapimagesv2/hunglvl3_45.jpg"
      else:
        the_color_array[6][0] = f"mapimagesv2\hunglvl3_67.jpg"
        the_color_array[5][0] = f"mapimagesv2\hunglvl3_56.jpg"
        the_color_array[4][0] = f"mapimagesv2\hunglvl3_45.jpg"

    if s.h >= 70:
      if os.name == "posix":
        the_color_array[6][0] = f"mapimagesv2/hunglvl4_67.jpg"
        the_color_array[5][0] = f"mapimagesv2/hunglvl4_56.jpg"
        the_color_array[4][0] = f"mapimagesv2/hunglvl4_45.jpg"
      else:
        the_color_array[6][0] = f"mapimagesv2\hunglvl4_67.jpg"
        the_color_array[5][0] = f"mapimagesv2\hunglvl4_56.jpg"
        the_color_array[4][0] = f"mapimagesv2\hunglvl4_45.jpg"

    if s.h >= 85:
      if os.name == "posix":
        the_color_array[6][0] = f"mapimagesv2/hunglvl5_67.jpg"
        the_color_array[5][0] = f"mapimagesv2/hunglvl5_56.jpg"
        the_color_array[4][0] = f"mapimagesv2/hunglvl5_45.jpg"
      else:
        the_color_array[6][0] = f"mapimagesv2\hunglvl5_67.jpg"
        the_color_array[5][0] = f"mapimagesv2\hunglvl5_56.jpg"
        the_color_array[4][0] = f"mapimagesv2\hunglvl5_45.jpg"

    # the_color_array [2][2] = red
    # the_color_array [2][3] = red
    # the_color_array [3][3] = red
    # the_color_array [3][2] = "mapimages\mapslice_01.png"
    # the_string_array[2][3] = "Urban"

    # the_color_array [5][3] = orange
    # the_color_array [5][5] = orange
    # the_color_array [5][4] = "house.jpg"
    # the_string_array[5][3] = "Sub-"
    # the_string_array[5][5] = "urban"

    # the_color_array [2][5] = yellow
    # the_color_array [3][5] = "farm.jpg"
    # the_string_array[2][5] = "Rural"

    caption= str(s.crisisMSG) + '\n' + str(s.operMSG) + '\n\n' + str(s.goal_message()) + str(s)
    print(caption)
    the_state_array = STATE_ARRAY(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
    # redraw.Redraw.drawcanvas()
    # redraw.Redraw.alert("ope")

print("TheHungerGame VIS file has been imported.")
    

    
