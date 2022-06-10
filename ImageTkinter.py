from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance

root = Tk()
frame = Frame(root, pady=50, padx=50)

global photo;

def getFile():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select an image")
    img = Image.open(file_path)
    resized_image = img.resize((400, 255), Image.ANTIALIAS)
    one = ImageTk.PhotoImage(resized_image.convert("RGB"))
    root.one = one
    root.img = img
    canvas1.create_image(0, 0, image=one, anchor='nw')

def enhanceImage():
    enhancer = ImageEnhance.Brightness(root.img)
    #brightness factor == 3
    img = enhancer.enhance(3)
    resized_image = img.resize((400, 255), Image.ANTIALIAS)
    two = ImageTk.PhotoImage(resized_image.convert("RGB"))
    root.two = two
    canvas2.create_image(0, 0, image=two, anchor='nw')
    
   
   
actualLabel = Label(frame, text="Uploaded Image")
brightenedLabel = Label(frame, text="Enhanced Image")

actualLabel.grid(row=0, column=0, sticky='')
brightenedLabel.grid(row=0, column=1, sticky='')

canvas1 = Canvas(frame, width=400, height=250, bg="black")
canvas1.grid(row=1, column=0)

canvas2 = Canvas(frame, width=400, height=250, bg="black")
canvas2.grid(row=1, column=1)

loadButton = Button(frame, command=getFile, text="Upload")
loadButton.grid(row=2, column=0, pady=10)

enhanceButton = Button(frame, text="Enhance", command=enhanceImage)
enhanceButton.grid(row=3, column=0, columnspan=2)


frame.pack()
root.mainloop();