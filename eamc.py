import tkinter
from PIL import Image, ImageTk
import io
from PIL import ImageDraw

root = tkinter.Tk()
root.geometry("600x300")

def clearup():
    print("nob")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", clearup)

myCanvas = tkinter.Canvas(root, bg="blue", height=600, width=300) #, tki=None, img=None, draw=None, imc=None)
myCanvas.img = Image.new(size=[600,300],mode="RGB")
myCanvas.draw = ImageDraw.Draw(myCanvas.img)
#myCanvas.draw.line((0, 0) + myCanvas.img.size, fill=128)
#myCanvas.draw.line((0, myCanvas.img.size[1], myCanvas.img.size[0], 0), fill=128)
myCanvas.tki = ImageTk.PhotoImage(myCanvas.img, height=myCanvas.img.height, width=myCanvas.img.width)
myCanvas.imc = myCanvas.create_image((0,0),image=myCanvas.tki, anchor="nw")	

myCanvas.pack(expand=True,fill="both")


last = None


def motion(event):
    global myCanvas, draw, image_container, last, img, tkimg 
    if event.state == 8: last = None
    if event.state | 256 == event.state:
        if last is None:
            last = [event.x, event.y]
        else:
            #tkimg = ImageTk.PhotoImage(img, height=img.height, width=img.width)
            myCanvas.draw.line((last[0], last[1], event.x,event.y), fill=255)
            myCanvas.tki = ImageTk.PhotoImage(myCanvas.img, height=myCanvas.img.height, width=myCanvas.img.width)
            myCanvas.create_image((0,0),image=myCanvas.tki, anchor="nw")
            last = [event.x, event.y]
    if event.state | 1024 == event.state: print("but2")
    #print(f"{event.x},{event.y},{event.state}")
    #print(dir(event))

root.bind("<Motion>", motion)


root.mainloop()