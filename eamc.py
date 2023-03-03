import tkinter
from PIL import Image, ImageTk, ImageDraw
import uuid

class Scribbler():

    def __init__(self, _root, main=False):

        self.main = main
        self.id = str(uuid.uuid4())
        self.root = _root
        self.master = tkinter.Toplevel(self.root)
        self.master.id =self.id
        self.frame = tkinter.Frame(self.master)

        self.width, self.height = 600, 300

        #self.root = tkinter.Tk()
        self.master.geometry(f"{self.width}x{self.height}")

        # init canvas 
        self.main_canvas = tkinter.Canvas(self.master, bg="blue") #, height=200, width=200) #, tki=None, img=None, draw=None, imc=None)

        # new pillow img and attach to canvas
        self.main_canvas.img = Image.new(size=[self.width,self.height],mode="RGBA")
        self.main_canvas.draw = ImageDraw.Draw(self.main_canvas.img)
        self.main_canvas.tki = ImageTk.PhotoImage(self.main_canvas.img, height=self.height, width=self.width)
        self.main_canvas.imc = self.main_canvas.create_image((0,0),image=self.main_canvas.tki, anchor="nw")	

        self.main_canvas.pack(expand=True,fill="both")
        self.last = None

        self.master.bind("<Motion>", self.motion)

        # clearup code run 
        # intercept the delete window and call function

        self.master.protocol("WM_DELETE_WINDOW", self.clearup)
        self.frame.pack()

    def clearup(self):
        print("nob")
        self.main_canvas.img.save(f"exit-{self.master.id}.png")
        self.master.destroy()
        if self.main:
            if len([c.id for c in list(self.root.children.values())])==0:
                self.root.destroy()

    def motion(self, event):
        if event.state == 8: self.last = None
        if event.state | 256 == event.state: # bitwise check on button press
            if self.last is None:
                self.last = [event.x, event.y]
            else:
                #tkimg = ImageTk.PhotoImage(img, height=img.height, width=img.width)
                # update pillow image rather than the image in the canvas
                self.main_canvas.draw.line((self.last[0], self.last[1], event.x,event.y), fill=(255,255,0,255))
                #i1.paste(i2, mask=i2) 
                # redo the tkimage
                self.main_canvas.tki = ImageTk.PhotoImage(self.main_canvas.img, height=self.height, width=self.width)
                self.main_canvas.create_image((0,0),image=self.main_canvas.tki, anchor="nw")
                self.last = [event.x, event.y]
        if event.state | 1024 == event.state: print("but2")
        #print(f"{event.x},{event.y},{event.state}")
        #print(dir(event))

if __name__=="__main__":
    root = tkinter.Tk()
    root.withdraw()
    app = Scribbler(root, main=True)
    root.mainloop()
else:
    root = tkinter.Tk()