# Create Caesar Wheel

# dependencies
from tkinter import *           # Python GUI library
from PIL import ImageTk         # Tkinter compatible PIL image module
from PIL import Image as im     # For Image manipulation
import numpy as np              # vector calculations

#functions

def getkey(ang):
    return int(ang/14)

def getpoints(ang):
    x1 = 300
    y1 = 300
    rad = ((ang-90)*np.pi)/180
    x2 = x1 + np.cos(rad)*140
    y2 = y1 + np.sin(rad)*140
    return (x2,y2)

def encrypt(text,length,key):
    for i in range(length):
        if text[i].isalpha():
            if text[i] >= 'a':
                temp = (ord(text[i])-97 + key)%26 + 97
            else:
                temp = (ord(text[i])-65 + key)%26 + 65
            text[i] = chr(temp)
    return "".join(text)

def decrypt(text,length,key):
    for i in range(length):
        if text[i].isalpha():
            if text[i] >= 'a':
                temp = ord(text[i])-97-(key%26)
                if temp < 0:
                    temp = 26 + temp
                text[i] = chr(temp+97)
            else:
                temp = ord(text[i])-65-(key%26)
                if temp < 0:
                    temp = 26 + temp
                text[i] = chr(temp+65)
    return "".join(text)
    
def update(key):
    
    val = v.get()
    if val == 0:
        text = textentry.get("1.0","end")
        text = list(text)
        length = len(text)
        text = encrypt(text,length,key)
        disp.delete("1.0","end")
        disp.insert(END,text.upper())
    elif val == 1:
        text = disp.get("1.0","end")
        text = list(text)
        length = len(text)
        text = decrypt(text,length,key)
        textentry.delete("1.0","end")
        textentry.insert(END,text.lower())
    

def getimage(image,ang):
    if ang == 0:
        img = image
    else:
        img = image.rotate(-ang+6)
    img.save('./materials/rotated.png') # Saving the rotated image
    return im.open('./materials/rotated.png') # returning the image
    
def getmag(x):
    return np.sqrt(x.dot(x))    # To calculate the length of a vector

def getangle(event):
    point = np.array([event.x,event.y])
    origin = np.array([300,300])
    a = np.array([0,-100])      # Referencial vector
    b = point - origin
    cos = a.dot(b)/(getmag(a)*getmag(b))
    rad = np.arccos(cos)
    ang = rad*180/np.pi
    if point[0] < 300:
        ang = 360 - ang
    angdict['ang'] = int(ang)
    #print(point)

if __name__ == "__main__":
    # initialize tkinter object
    tk = Tk()
    tk.geometry("800x800")
    # The main frame
    frame = Frame(tk,width=800,height=800,bd=1)
    frame.pack()

    # Setting Tkinter variable
    v = IntVar()

    # frame for radio buttons
    tframe = Frame(frame)
    tframe.pack(expand=1,fill=X,pady=1,padx=100)

    # setting the radio options
    r1 = Radiobutton(tframe,text="Encrypt",padx=20,variable=v, value=0)
    r1.pack(side=LEFT)
    r2 = Radiobutton(tframe,text="Decrypt",padx=40,variable=v, value=1)
    r2.pack()
    
    # set up frame to hold options
    rframe = Frame(frame,bd=2,relief=RAISED)
    rframe.pack(side=LEFT,expand=1,pady=1,padx=1)

    # The text message
    text = Label(rframe,
                 text = "The Plain Text",
                 fg='black',
                 font='Times 15',
                 bg='white')
<<<<<<< HEAD
    text.pack(fill=X,expand=1,pady=1,padx=100)
    textentry = Text(frame,height=5,width=70,font='Times 15')
    textentry.pack(expand=1,padx=100)

    # set up frame to hold options
    rframe = Frame(frame)
    rframe.pack(expand=1,fill=X,pady=1,padx=100)
    
    # setting the radio options
    r1 = Radiobutton(rframe,text="Encrypt",padx=20,variable=v, value=0)
    r1.pack(side=LEFT)
    r2 = Radiobutton(rframe,text="Decrypt",padx=40,variable=v, value=1)
    r2.pack()
=======
    text.pack(fill=X,expand=1,pady=1,padx=10)
    textentry = Text(rframe,height=40,width=35,font='Times 15')
    textentry.pack(expand=1,padx=1)  
>>>>>>> 7d6017a30219efebfb99ae829837580842342f45
    
    # Frame to hold the canvas
    iframe = Frame(frame,bd=2,relief=RAISED)
    iframe.pack(side=LEFT,expand=1,fill=BOTH,pady=10,padx=5)
    
    # Set up the canvas
    canvas = Canvas(iframe,width=600,height=600)
    tk.title("Caesar's Wheel")
    canvas.pack()

    # labels
    canvas.create_text(290,220,fill="darkblue",font="Times 15",
                       text = "Inner Circle: Plain Text")
    canvas.create_text(120,10,fill="darkblue",font="Times 15",
                       text = "Outer Circle: Cipher Text")

    tlframe = Frame(frame,bd=2,relief=RAISED)
    tlframe.pack(side=LEFT,expand=1,padx=5)

    # setting the end message
    displabel = Label(tlframe,
                      text = "The Cipher text",
                      fg='black',
                      font='Times 15',
                      bg='white')
    displabel.pack(fill=X,expand=1,pady=1,padx=50)
    disp = Text(tlframe,height=40,width=35,font='Times 15')
    disp.pack(expand=1,padx=1)
    
    image1 = im.open("./materials/outerCircle.png")
    image2 = im.open("./materials/innerCircle.png")
    
    tkimage2 = ImageTk.PhotoImage(image2)
    imgobj2 = canvas.create_image(300,300,image=tkimage2)
    angdict = {'ang': 0}
    
    while True:
        #print(angdict['ang'])
        img = getimage(image1,angdict['ang'])
        tkimage1 = ImageTk.PhotoImage(img)
        imgobj1 = canvas.create_image(300,300,image=tkimage1)
        (x,y) = getpoints(angdict['ang'])
        line = canvas.create_line(300,300,x,y,arrow=LAST)
        canvas.update()
        key = getkey(angdict['ang'])        
        #print("key: ",key," option: ",v.get())
        update(key)     # encrypt/decrypt  with key
        canvas.bind("<Button-1>",getangle)
        canvas.delete(imgobj1)
        canvas.delete(line)
        
