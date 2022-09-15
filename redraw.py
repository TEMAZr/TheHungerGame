import tkinter as tk
import Tk_SOLUZION_Client3 as tks3
from time import sleep
from PIL import ImageTk, Image

l = []

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
        newcanvas.create_text(250, 250, text=text, justify="center")
        newcanvas.pack()
    
    @staticmethod
    def soloalert(window, text, timeout=None):
        # useful https://stackoverflow.com/questions/15306222/automatically-close-window-after-a-certain-time
        # this one too https://stackoverflow.com/questions/14336472/how-to-create-new-tkinter-window-after-mainloop
        print("Attempting solo alert")
        newwindow = tk.Toplevel(window)
        newwindow.geometry("500x500")
        newwindow.title("Alert!")
        newcanvas = tk.Canvas(newwindow, width=500, height=500)
        newcanvas.create_text(250, 250, text=text, font=("Helvetica",48,"bold"),justify="center")
        newcanvas.pack()
        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)
    
    @staticmethod
    def terminatemessage(window, text, timeout=None):
        # useful https://stackoverflow.com/questions/15306222/automatically-close-window-after-a-certain-time
        # this one too https://stackoverflow.com/questions/14336472/how-to-create-new-tkinter-window-after-mainloop
        print("Attempting termination message")
        newwindow = tk.Toplevel(window)
        newwindow.geometry("500x500+500+0")
        newwindow.title("Alert!")
        newcanvas = tk.Canvas(newwindow, width=500, height=500)
        newcanvas.create_text(250, 250, text=text, font=("Helvetica",12), width=300, justify='center')
        newcanvas.pack()
        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

    @staticmethod
    def crisisalert(window, crisis, timeout=None):
        # TODO: Fix whatever the heck is going on, it's not displaying correctly
        print("Attempting crisis alert")

        newwindow = tk.Toplevel(window)
        newwindow.geometry("500x500")
        newwindow.title("Crisis Alert!")

        image = Image.open('alert.png')
        image = image.resize((150,150), Image.Resampling.LANCZOS)
        testimg = ImageTk.PhotoImage(image)
        l.append(testimg)

        canvas = tk.Canvas(newwindow,width=500, height=500, bg="red")
        canvas.pack()
        canvas.create_image(250, 150, image=testimg)

        canvas.create_text(250, 50, text="CRISIS ALERT", fill="white", font=("Helvetica",36,"bold"))

        canvas.create_text(250, 360, text=crisis.msg, fill="white",width=350, font=(24),justify='center')

        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

    @staticmethod
    def imagewindow(window):
        pass
