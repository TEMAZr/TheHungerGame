'''Missionaries3_VIS_FOR_TK3.py
Version of Sept. 17, 2019.
This visualization file works with Missionaries3.py and
Tk_SOLUZION_Client3.py.
It uses three jpg images for showing missionaries, cannibals, and the boat.

'''
from tkinter import font

myFont=None

WIDTH = 700
HEIGHT = 500
TITLE = 'The Hunger Game'

STATE_WINDOW = None
STATE_ARRAY = None

def initialize_vis(st_win, state_arr, initial_state):
  global STATE_WINDOW, STATE_ARRAY
  STATE_WINDOW = st_win
  STATE_ARRAY = state_arr
  STATE_WINDOW.winfo_toplevel().title(TITLE)
  render_state(initial_state)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    #print("In render_state, state is "+str(s))
    # Create the default array of colors

    green = (62, 137, 20)
    blue = (3, 94, 123)
    
    red = (244, 68, 46)
    orange = (248, 102, 36)
    yellow = (234, 196, 53)
    
    row = [green]* 7
    the_color_array = [row, row[:], row[:], row[:], row[:], row[:], row[:]]
    
    # Now create the default array of string labels.
    row = ['' for i in range(7)]
    the_string_array = [row, row[:], row[:], row[:], row[:], row[:], row[:]]

    #top task bar
    for i in range(7): 
      the_color_array [0][i] = blue

    #side hunger bar
    the_color_array [2][0] = blue
    the_color_array [3][0] = blue
    the_string_array[2][0] = "Hunger:"
    the_string_array[3][0] = str(s.h) + "%"

    # Adjust colors and strings to match the state.
    the_color_array [0][0] = "calendar.jpg"
    the_string_array[0][0] = "2022"
    
    the_color_array [0][1] = "money.jpg"
    the_string_array[0][1] = "$" + str(s.m)

    the_color_array [2][2] = red
    the_color_array [2][3] = red
    the_color_array [3][3] = red
    the_color_array [3][2] = "building.jpg"
    the_string_array[2][3] = "Urban"

    the_color_array [5][3] = orange
    the_color_array [5][5] = orange
    the_color_array [5][4] = "house.jpg"
    the_string_array[5][3] = "Sub-"
    the_string_array[5][5] = "urban"

    the_color_array [2][5] = yellow
    the_color_array [3][5] = "farm.jpg"
    the_string_array[2][5] = "Rural"

    caption="Current state of the puzzle. Textual version: "+str(s)
    print(caption)
    the_state_array = STATE_ARRAY(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()

print("TheHungerGame VIS file has been imported.")
    

    
