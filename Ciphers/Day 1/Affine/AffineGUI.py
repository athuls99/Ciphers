from AffineCipher import encrypt,decrypt,gcd
import tkinter as tk
from tkinter import ttk
from wordsegment import load,segment
import re

class Start:
    def __init__(self,master):
        self.frame = tk.Frame(master,width=700,height=200)
        self.frame.pack(pady=1,padx=10)
        labelA = tk.Label(self.frame,text="Value of a ",fg="black",font="Arial 15")
        self.a = tk.Text(self.frame,height=1,width=5,font="Times 15")
        labelB = tk.Label(self.frame,text="Value of b ",fg="black",font="Arial 15")
        self.b = tk.Text(self.frame,height=1,width=5,font="Times 15")
        labelA.pack(side=tk.LEFT,padx=5)
        self.a.pack(side=tk.LEFT,padx=1)
        labelB.pack(side=tk.LEFT,padx=5)
        self.b.pack(side=tk.LEFT,padx=1)

class Cipher:
    def __init__(self,master,obj):
        self.k = obj.a
        self.b = obj.b
        self.msg = ""

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
        chk = self.check()
        if type(chk) == tuple:
            text = get(self.text)
            text = re.sub(r'[^A-Za-z]',"",text)
            etext = encrypt(text.upper(),chk[0],chk[1])
            self.etext.delete("1.0","end")
            self.etext.insert(tk.END,etext)
    
    def dec(self):
        chk = self.check()
        if type(chk) == tuple:
            etext = get(self.etext)
            etext = re.sub(r'[^A-Za-z]',"",etext)
            text = decrypt(etext.upper(),chk[0],chk[1])
            text = " ".join(segment(text))
            self.text.delete("1.0","end")
            self.text.insert(tk.END,text.lower())

    def popup(self):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=self.msg, font="Verdana 10")
        label.pack(side="top", fill="x", pady=10,padx=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def check(self):
        k = int(get(self.k))
        b = int(get(self.b))
        if gcd(k,26) != 1:
            self.msg="Invalid value,please enter a co-prime of 26"
            self.popup()
            return 0
        return (k,b)
    
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
    window.title("Affine Cipher")
    #window.geometry("700x700")
    sobj = Start(window)
    enc = Cipher(window,sobj)
    window.mainloop()