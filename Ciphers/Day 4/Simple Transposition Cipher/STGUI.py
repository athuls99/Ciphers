from SimpleTranspositionCipher1 import encrypt as en1,decrypt as de1
from SimpleTranspositionCipher2 import encrypt as en2, decrypt as de2
import tkinter as tk
from tkinter import ttk
from wordsegment import load,segment

class Start:
    def __init__(self,master):
        self.v = tk.IntVar()
        self.frame = tk.Frame(master,width=700,height=200)
        self.frame.pack(pady=1,padx=10)
        label = tk.Label(self.frame,text="The type of Simple Transposition Cipher",fg="black",font="Arial 15")
        label.pack(pady=5)
        r1 = tk.Radiobutton(self.frame,text="String",padx=20,variable=self.v, value=0,font="Arial 13")
        r1.pack(side=tk.LEFT,padx=5,pady=10)
        r2 = tk.Radiobutton(self.frame,text="Word",padx=40,variable=self.v, value=1,font="Arial 13")
        r2.pack(padx=1,pady=10)

class Cipher:
    def __init__(self,master,obj):
        self.v = obj.v

        # for encrypt
        self.frame = tk.Frame(master,bd=1,relief=tk.RAISED)
        self.frame.pack(expand=1,side=tk.LEFT,pady=5,padx=10,fill=tk.X)
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1)
        label = tk.Label(iframe,text="Plain text",font="Times 20 bold")
        label.pack(padx=10)
        self.ebutton = tk.Button(iframe,text="Encrypt",command=self.enc,font="Arial 15")
        self.ebutton.pack(side=tk.LEFT,padx=10)
        self.ebutton = tk.Button(iframe,text="Clear",command=lambda: self.clear(0),font="Arial 15")
        self.ebutton.pack(padx=10)
        self.text = tk.Text(self.frame,height=40,width=65,fg="black",font="Times 15")
        self.text.pack(padx=10,pady=1)
        

        # for decrypt
        self.frame = tk.Frame(master,bd=1,relief=tk.RAISED)
        self.frame.pack(expand=1,pady=5,padx=10,fill=tk.X)
        eframe = tk.Frame(self.frame)
        eframe.pack(expand=1)
        label = tk.Label(eframe,text="Cipher text",font="Times 20 bold")
        label.pack(padx=10)
        self.dbutton = tk.Button(eframe,text="Decrypt",command=self.dec,font="Arial 15")
        self.dbutton.pack(side=tk.LEFT,padx=10)
        self.dbutton = tk.Button(eframe,text="Clear",command=lambda: self.clear(1),font="Arial 15")
        self.dbutton.pack(padx=10)
        self.etext = tk.Text(self.frame,height=40,width=65,fg="black",font="Times 15")
        self.etext.pack(padx=10,pady=1)
    
    def enc(self):
        text = get(self.text)
        v = self.v.get()
        if v == 0:
            etext = en1(text)
        elif v == 1:
            etext = en2(text)
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext.upper())
    
    def dec(self):
        etext = get(self.etext)
        v = self.v.get()
        if v == 0:
            text = de1(etext)
        elif v == 1:
            text = de2(etext)
        self.text.delete("1.0","end")
        self.text.insert(tk.END,text.lower())

    def clear(self,opt):
        if opt == 0:
            self.text.delete("1.0","end")
        else:
            self.etext.delete("1.0","end")
        

def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    load()
    window = tk.Tk()
    window.title("Simple Transposition Cipher")
    #window.geometry("700x700")
    sobj = Start(window)
    enc = Cipher(window,sobj)
    window.mainloop()
