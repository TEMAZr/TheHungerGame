import tkinter as tk
import Tk_SOLUZION_Client3 as tks3
from time import sleep

class Redraw:
    holdwindow = None
    w = 0
    h = 0
    canvas = None
    counter = 0
    colors = ["blue", "red", "yellow"]

    def __init__(self, canvas, w, h, window):
        Redraw.w = w
        Redraw.h = h
        print("Redraw initialised")
        Redraw.canvas = canvas
        Redraw.holdwindow = window
    
    @staticmethod
    def drawcanvas():
        print("Redrawn")
        Redraw.canvas.delete("all")
        Redraw.canvas.configure(bg=Redraw.colors[Redraw.counter])
        Redraw.canvas.create_text(200,200, text=f"Length of applicability vector: {tks3.APPLICABILITY_VECTOR}")
        Redraw.counter += 1

    @staticmethod
    def alert(text):
        print("Attempting alert")
        newwindow = tk.Toplevel(Redraw.holdwindow)
        newwindow.geometry("500x500")
        newwindow.title("Alert!")
        newcanvas = tk.Canvas(newwindow, width=500, height=500)
        newcanvas.create_text(250, 250, text=text)
        sleep(2)
        newwindow.destroy()
