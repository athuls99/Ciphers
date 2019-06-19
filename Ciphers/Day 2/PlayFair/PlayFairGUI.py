from playfairCipher import preprocess,encryptMessage,decryptMessage,removeX
import tkinter as tk
from tkinter import ttk
from wordsegment import load,segment

class Start:
    def __init__(self,master):
        self.frame = tk.Frame(master,width=700,height=200)
        self.frame.pack(pady=1,padx=10)
        labelA = tk.Label(self.frame,text="Key ",fg="black",font="Arial 15")
        self.a = tk.Text(self.frame,height=1,width=15,font="Times 15")
        labelA.pack(side=tk.LEFT,padx=5)
        self.a.pack(side=tk.LEFT,padx=1)

class Cipher:
    def __init__(self,master,obj):
        self.k = obj.a
        self.msg = ""

        # for encrypt
        self.frame = tk.Frame(master,width=650,height=200,bd=1,relief=tk.RAISED)
        self.frame.pack(pady=25,padx=10,fill=tk.X)
        self.text = tk.Text(self.frame,height=5,width=50,fg="black",font="Times 15")
        self.text.pack(side=tk.LEFT,padx=10,pady=15)
        eframe = tk.Frame(self.frame)
        eframe.pack(expand=1)
        self.ebutton = tk.Button(eframe,text="Encrypt",command=self.enc,font="Arial 20")
        self.ebutton.pack(padx=10,pady=10)
        self.ebutton = tk.Button(eframe,text="Clear",command=lambda: self.clear(0),font="Arial 18")
        self.ebutton.pack(padx=10,pady=10)

        # for decrypt
        self.frame = tk.Frame(master,width=650,height=200,bd=1,relief=tk.RAISED)
        self.frame.pack(pady=5,padx=10,fill=tk.X)
        self.etext = tk.Text(self.frame,height=5,width=50,fg="black",font="Times 15")
        self.etext.pack(side=tk.LEFT,padx=10,pady=15)
        dframe = tk.Frame(self.frame)
        dframe.pack(expand=1)
        self.dbutton = tk.Button(dframe,text="Decrypt",command=self.dec,font="Arial 20")
        self.dbutton.pack(padx=10,pady=10)
        self.ebutton = tk.Button(dframe,text="Clear",command=lambda: self.clear(1),font="Arial 18")
        self.ebutton.pack(padx=10,pady=10)
    
    def enc(self):
        text = get(self.text)
        key = get(self.k)
        (encrypt,ind) = preprocess(0,text.upper(),key.upper())
        etext = encryptMessage(encrypt,ind)
        etext = "".join(etext).upper()
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext)
    
    def dec(self):
        etext = get(self.etext)
        key = get(self.k)
        (encrypt,ind) = preprocess(1,etext.upper(),key.upper())
        text = decryptMessage(encrypt,ind)
        text = removeX(text)
        text = segment("".join(text))
        text = " ".join(text).lower()
        self.text.delete("1.0","end")
        self.text.insert(tk.END,text)

    def popup(self):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=self.msg, font="Verdana 10")
        label.pack(side="top", fill="x", pady=10,padx=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    
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
    window.title("PlayFair Cipher")
    #window.geometry("700x700")
    sobj = Start(window)
    enc = Cipher(window,sobj)
    window.mainloop()