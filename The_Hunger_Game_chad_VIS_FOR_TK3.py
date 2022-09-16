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
from The_Hunger_Game_chad import State

myFont=None

WIDTH = int(2732*0.3)-5
HEIGHT = int(2048*0.3)-6
TITLE = 'The Hunger Game'

STATE_WINDOW = None
STATE_ARRAY = None
ROOT = None
THE_CANVAS = None

blank = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
        ]

truskmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,1,2,3,0,0,5,6,0],
  [0,0,0,0,0,4,0,0,0,0,0],
  [0,0,7,8,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,9,10,0,0,0],
  [0,0,11,12,0,0,0,0,15,16,0],
  [0,0,13,14,0,0,0,17,18,0,0]
        ]

windmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,1,2,3,0,0,0,0,8,9],
  [0,0,4,5,6,0,0,0,0,0,10],
  [0,0,7,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
        ]

roadmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,1,2,0,0,0,0],
  [0,0,0,0,3,4,5,0,7,8,0],
  [0,0,0,0,6,0,0,0,9,10,0],
  [0,0,0,0,11,12,0,0,0,0,0],
  [0,0,0,0,13,14,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
        ]

stimulusmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,2,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,3,4,0,0,0,0,5,6,0],
  [0,0,0,0,0,0,0,0,7,8,0],
  [0,0,0,0,0,0,0,0,0,0,0]
]
  
factorymatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,1,0,0,0,0,0,0,0],
  [0,0,0,2,3,4,0,0,0,0,0],
  [0,0,0,5,6,7,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,8,0,0,0],
  [0,0,0,0,9,10,11,12,0,0,0],
  [0,0,0,0,13,14,15,16,0,0,0]
        ]

campaignmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,2,0,0,0],
  [0,0,3,0,0,0,0,0,0,0,0],
  [0,0,4,0,0,0,0,0,5,6,0],
  [0,0,0,0,0,0,0,0,7,8,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
        ]

beematrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,1,0,0,2,0,0,0,3,0,0],
  [0,4,0,0,0,0,0,0,5,0,0],
  [0,0,0,0,0,6,0,0,0,7,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,8,0,0,0,0,0,0,0],
  [0,0,9,0,10,0,0,0,0,11,0]
        ]

holesmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,1,2,3,0,0,0,0,0],
  [0,0,0,4,5,6,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
        ]

billmatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,2,3,4,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
        ]

gmomatrix = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,2,0,0],
  [0,5,6,7,0,0,0,3,4,0,0],
  [0,8,9,10,11,0,0,12,13,0,0],
  [0,0,0,0,0,0,0,14,15,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
        ]


def initialize_vis(st_win, state_arr, initial_state):
  global STATE_WINDOW, STATE_ARRAY, ROOT, THE_CANVAS, WIDTH, HEIGHT
  # State.holdwindow = ROOT
  STATE_WINDOW = st_win
  STATE_ARRAY = state_arr
  STATE_WINDOW.winfo_toplevel().title(TITLE)
  # r = redraw.Redraw(STATE_WINDOW.master, WIDTH, HEIGHT)
  render_state(initial_state)
  redraw.Redraw.welcomewindow(ROOT, 20000)

def give_canvas(canvas, window):
  r = redraw.Redraw(canvas, WIDTH, HEIGHT, window)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont, truskmatrix
    if not myFont:
        myFont = font.Font(family="Helvetica", size=12)
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


    if State.last_news is not None and State.last_news.find("wind farm") != -1:
      for i in range(8):
        for j in range(11):
          if windmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"wind/wind{windmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"wind\wind{windmatrix[i][j]}.jpg"

    if State.last_news is not None and State.last_news.find("roads") != -1:
      for i in range(8):
        for j in range(11):
          if roadmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"roads/roads{roadmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"roads\roads{roadmatrix[i][j]}.jpg"

    if State.last_news is not None and State.last_news.find("stimulus check") != -1:
      for i in range(8):
        for j in range(11):
          if stimulusmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"stimulus/sc{stimulusmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"stimulus\sc{stimulusmatrix[i][j]}.jpg"

    if State.last_news is not None and State.last_news.find("mechanize") != -1:
      for i in range(8):
        for j in range(11):
          if factorymatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"factory/factory{factorymatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"factory\\factory{factorymatrix[i][j]}.jpg"

    if State.last_news is not None and State.last_news.find("pestered") != -1:
      for i in range(8):
        for j in range(11):
          if campaignmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"campaign/campaign{campaignmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"campaign\campaign{campaignmatrix[i][j]}.jpg"

    if s.crisis is not None and s.crisis.name == "Homicidal Hornets":
      for i in range(8):
        for j in range(11):
          if beematrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"hornets/hornet{beematrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"hornets\hornet{beematrix[i][j]}.jpg"

    if s.crisis is not None and s.crisis.name == "Surprise Sinkhole":
      for i in range(8):
        for j in range(11):
          if holesmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"sinkhole/hole{holesmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"sinkhole\hole{holesmatrix[i][j]}.jpg"

    if s.crisis is not None and s.crisis.name == "Billionaire Blowout!":
      for i in range(8):
        for j in range(11):
          if billmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"billionaires/bill{billmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"billionaires\bill{billmatrix[i][j]}.jpg"
    
    if State.last_news is not None and State.last_news.find("alien") != -1:
      for i in range(8):
        for j in range(11):
          if gmomatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"gmos/gmos{gmomatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"gmos\gmos{gmomatrix[i][j]}.jpg"

# stimulusmatrix, factorymatrix, campaignmatrix, beematrix, holesmatrix, billmatrix, gmomatrix
    if s.rocket_truck:
      for i in range(8):
        for j in range(11):
          if truskmatrix[i][j] != 0:
            if os.name == "posix":
              the_color_array[i][j] = f"elontrusk/elontrusk{truskmatrix[i][j]}.jpg"
            else:
              the_color_array[i][j] = f"elontrusk\elontrusk{truskmatrix[i][j]}.jpg"

    caption= str(s)
    print(caption)
    the_state_array = STATE_ARRAY(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    
    if s.crisis is not None and s.crisis.turns_active == 1:
      print("\033[31;1;4mA crisis is happening\033[0m")
      # print(type(State.holdwindow))
      redraw.Redraw.crisisalert(State.holdwindow, s.crisis, 10000)
    the_state_array.show()
    # redraw.Redraw.drawcanvas()
    # redraw.Redraw.alert("ope")

print("TheHungerGame VIS file has been imported.")
    

    
