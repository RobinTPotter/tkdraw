import tkinter
from PIL import Image, ImageTk, ImageDraw

root = tkinter.Tk()
root.geometry("600x300")

# init canvas 
myCanvas = tkinter.Canvas(root, bg="blue", height=600, width=300) #, tki=None, img=None, draw=None, imc=None)

# new pillow img and attach to canvas
myCanvas.img = Image.new(size=[600,300],mode="RGBA")
myCanvas.draw = ImageDraw.Draw(myCanvas.img)
#myCanvas.draw.line((0, 0) + myCanvas.img.size, fill=128)
#myCanvas.draw.line((0, myCanvas.img.size[1], myCanvas.img.size[0], 0), fill=128)
myCanvas.tki = ImageTk.PhotoImage(myCanvas.img, height=myCanvas.img.height, width=myCanvas.img.width)
myCanvas.imc = myCanvas.create_image((0,0),image=myCanvas.tki, anchor="nw")	

myCanvas.pack(expand=True,fill="both")

# clearup code run 

def clearup():
    print("nob")
    myCanvas.img.save("exit.png")
    root.destroy()

# intercept the delete window and call function

root.protocol("WM_DELETE_WINDOW", clearup)



last = None


def motion(event):
    global myCanvas, draw, image_container, last, img, tkimg 
    if event.state == 8: last = None
    if event.state | 256 == event.state: # bitwise check on button press
        if last is None:
            last = [event.x, event.y]
        else:
            #tkimg = ImageTk.PhotoImage(img, height=img.height, width=img.width)
            # update pillow image rather than the image in the canvas
            myCanvas.draw.line((last[0], last[1], event.x,event.y), fill=(255,255,0,255))
            #i1.paste(i2, mask=i2) 
            # redo the tkimage
            myCanvas.tki = ImageTk.PhotoImage(myCanvas.img, height=myCanvas.img.height, width=myCanvas.img.width)
            myCanvas.create_image((0,0),image=myCanvas.tki, anchor="nw")
            last = [event.x, event.y]
    if event.state | 1024 == event.state: print("but2")
    #print(f"{event.x},{event.y},{event.state}")
    #print(dir(event))

root.bind("<Motion>", motion)


root.mainloop()