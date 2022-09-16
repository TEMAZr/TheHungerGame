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

    @staticmethod
    def newsreport(window, text, timeout=None):
        scale = 0.6
        newwindow = tk.Toplevel(window)
        newwindow.geometry(f"{int(600*scale)}x{int(600*scale)}+{int(newwindow.winfo_screenwidth()-600*scale)}+0")
        newwindow.title("Breaking News!")

        image = Image.open('newsbg.png')
        image = image.resize((int(600*scale),int(600*scale)), Image.Resampling.LANCZOS)
        testimg = ImageTk.PhotoImage(image)
        l.append(testimg)

        image2 = Image.open('money.jpg')
        image2 = image2.resize((int(180*scale),int(180*scale)), Image.Resampling.LANCZOS)
        image2 = image2.convert("L")
        moneyimg = ImageTk.PhotoImage(image2)
        l.append(moneyimg)

        image3 = Image.open('holyburger.png')
        image3 = image3.resize((int(135*scale),int(180*scale)), Image.Resampling.LANCZOS)
        image3 = image3.convert("L")
        burgerimg = ImageTk.PhotoImage(image3)
        l.append(burgerimg)

        canvas = tk.Canvas(newwindow,width=int(600*scale), height=int(600*scale), bg="white")
        canvas.pack()
        canvas.create_image(int(300*scale), int(300*scale), image=testimg)
        canvas.create_image(int(100*scale), int(500*scale), image=moneyimg)
        canvas.create_image(int(525*scale), int(275*scale), image=burgerimg)

        canvas.create_text(int(225*scale), int(275*scale), text=text, font=("century schoolbook", int(13*scale)), width=int(400*scale))

        canvas.create_text(int(330*scale), int(450*scale), text="This information has been researched for the development of this game; data, statistics, and facts mentioned come from government reports or independent studies.", font=("century schoolbook", int(10*scale)), width=int(230*scale))

        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

    @staticmethod
    def welcomewindow(window, timeout=None):
        newwindow = tk.Toplevel(window)
        newwindow.title("Welocome!")
        newwindow.geometry("650x450")

        canvas = tk.Canvas(newwindow, width=650, height=450, bg="white")
        canvas.pack()

        image = Image.open('weolcome.png')
        image = image.resize((500,81), Image.Resampling.LANCZOS)
        testimg = ImageTk.PhotoImage(image)
        l.append(testimg)

        canvas.create_image(325,80, image=testimg)

        eek = "Welocome to the Hunger Game! You find yourself in the town of Dennyville.\n\nThis city is in a crisis: hunger rates have spiked to a new high. You, as the god controlling this city, must help the citizens get hunger rates under control. You have various operators at your disposal, all of which cost or give you money. Help Dennyville lower its hunger rate under 30% as fast as possible! \n\nAs an extra challenge, random crises will occur, especially if the hunger rate is high... Good Luck!"

        canvas.create_text(325,250, text=eek,font=("helvetica",12),width=450,justify='center')

        btn = tk.Button(canvas, text="Start your journey, trainee god!", command=newwindow.destroy)
        btn.place(x=325-90, y=375)

        newwindow.attributes('-topmost', 'true')

        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

    @staticmethod
    def quick_facts(window, timeout=None):
        newwindow = tk.Toplevel(window)
        newwindow.title("American Hunger Quick Facts")
        newwindow.geometry(f"550x550+{int(newwindow.winfo_screenwidth()/2-275)}+0")

        canvas = tk.Canvas(newwindow, width=550, height=550, bg="white")
        canvas.pack()

        quick_facts = "It is bad for people to starve. Source: Michael\n\nIn 2021, 10.2 percent of households were food-insecure, and 3.8 percent had very low food security. These values have not experienced a significant decrease in the last twenty years.\n\nAlso in 2021, children were food-insecure in 6.2 percent of households with children.\n\nThe median food-secure household spends 16 percent more on food than food-insecure households of the same composition, including purchases made with food stamps.\n\nAbout 56 percent of food-insecure households participated in major federal nutrition assistance programs.\n\nHouseholds in rural areas experience increased food insecurity as compared to their suburban and urban counterparts.\n\nThe food insecurity rate is highest in the South (11.4 percent), followed by the Midwest (9.9 percent), West (9.7 percent), and Northeast (8.8 percent)."

        canvas.create_text(275, 275, text=quick_facts, fill="black",width=350, font=("helvetica",12),justify='center')

        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

    @staticmethod
    def losswindow(window, text, timeout=None):
        newwindow = tk.Toplevel(window)
        newwindow.title("get rekt, get gud")
        newwindow.geometry(f"900x900+{int(newwindow.winfo_screenwidth()/2-450)}+{0}")
        newwindow.protocol('WM_DELETE_WINDOW', lambda: newwindow.master.destroy())

        canvas = tk.Canvas(newwindow, width=1000, height=1000)
        canvas.pack()

        image = Image.open('failscreen.png')
        image = image.resize((800,800), Image.Resampling.LANCZOS)
        testimg = ImageTk.PhotoImage(image)
        l.append(testimg)

        canvas.create_image(450,420,image=testimg)

        canvas.create_text(450, 630, text=text, fill="white", font=("Helvetica",30,"bold"), justify='center', width=700)

        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

    @staticmethod
    def winwindow(window, text, timeout=None):
        newwindow = tk.Toplevel(window)
        newwindow.title("get rekt, get gud")
        newwindow.geometry(f"900x900+{int(newwindow.winfo_screenwidth()/2-450)}+{0}")
        newwindow.protocol('WM_DELETE_WINDOW', lambda: newwindow.master.destroy())

        canvas = tk.Canvas(newwindow, width=1000, height=1000)
        canvas.pack()

        image = Image.open('winscreen.png')
        image = image.resize((800,800), Image.Resampling.LANCZOS)
        testimg = ImageTk.PhotoImage(image)
        l.append(testimg)

        canvas.create_image(450,420,image=testimg)

        canvas.create_text(450, 630, text=text, fill="white", font=("Helvetica",30,"bold"), justify='center', width=700)

        if timeout is not None:
            newwindow.after(timeout, newwindow.destroy)

if __name__ == "__main__":
    #test stuff here
    window = tk.Tk()
    window.geometry("500x500")

    Redraw.quick_facts(window)

    # Redraw.winwindow(window,"Dennyville is ever grateful for your contributions! \n\nbye lul.")


    # Redraw.newsreport(window, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque volutpat, eros vel hendrerit malesuada, urna ex condimentum tortor, in imperdiet purus mi at turpis. Cras nec augue dignissim, aliquet ligula quis, commodo ligula. Mauris elementum leo eu consequat posuere. Sed vel magna eget urna sodales porttitor in vel leo.")
    window.mainloop()