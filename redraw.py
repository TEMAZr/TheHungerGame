import tkinter as tk

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
        tk.Misc.lift(Redraw.canvas)
        Redraw.counter += 1
