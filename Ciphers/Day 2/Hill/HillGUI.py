from functions import textEncDec,isPerfect,createMatrix,checkKey
import tkinter as tk
from tkinter import ttk
from wordsegment import load,segment

class Start:
    def __init__(self,master):
        self.frame = tk.Frame(master,width=700,height=200)
        self.frame.pack(pady=1,padx=10)
        labelA = tk.Label(self.frame,text="Key",fg="black",font="Arial 15")
        self.a = tk.Text(self.frame,height=1,width=35,font="Times 15")
        labelA.pack(side=tk.LEFT,padx=5)
        self.a.pack(padx=1)

class Cipher:
    def __init__(self,master,obj):
        self.key = obj.a
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
        if chk:
            text = get(self.text)
            etext = textEncDec(text.upper(),chk,0)
            self.etext.delete("1.0","end")
            self.etext.insert(tk.END,etext)
    
    def dec(self):
        chk = self.check()
        if chk:
            etext = get(self.etext)
            text = textEncDec(etext.upper(),chk,1)
            text = segment(text)
            self.text.delete("1.0","end")
            self.text.insert(tk.END,"".join(text))

    def clear(self,opt):
        if opt == 0:
            self.text.delete("1.0","end")
        else:
            self.etext.delete("1.0","end")

    def popup(self):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=self.msg, font="Verdana 10")
        label.pack(side="top", fill="x", pady=10,padx=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def check(self):
        key = get(self.key).upper()
        lKey = len(key)
        if isPerfect(lKey):
            order = int(lKey**(1/2))
            keyMat = createMatrix(key,order,0)
            det = keyMat.det()
            if checkKey(det):
                return key
            else:
                self.msg = "The Key is not invertible"
        else:
            self.msg = "The length of key should be Perfect Sqaure"
        self.popup()
        return False

def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    load()
    window = tk.Tk()
    window.title("Hill Cipher")
    #window.geometry("700x700")
    sobj = Start(window)
    enc = Cipher(window,sobj)
    window.mainloop()