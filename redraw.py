import tkinter as tk
import Tk_SOLUZION_Client3 as tks3

class Redraw:
    holdwindow = None
    w = 0
    h = 0
    canvas = None
    counter = 0
    colors = ["blue", "red", "yellow"]

    def __init__(self, canvas, w, h):
        Redraw.w = w
        Redraw.h = h
        print("Redraw initialised")
        Redraw.canvas = canvas
    
    @staticmethod
    def draw():
        print("Redrawn")
        Redraw.canvas.delete("all")
        Redraw.canvas.configure(bg=Redraw.colors[Redraw.counter])
        Redraw.canvas.create_text(200,200, text=f"Length of applicability vector: {len(tks3.APPLICABILITY_VECTOR)}")
        Redraw.counter += 1
