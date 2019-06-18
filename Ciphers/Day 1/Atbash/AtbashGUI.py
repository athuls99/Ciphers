from Atbash import Encryptor,Decryptor
import tkinter as tk
from tkinter import ttk

class Cipher:
    def __init__(self,master):
        self.msg = ""

        # for encrypt
        self.frame = tk.Frame(master,width=650,height=200,bd=1,relief=tk.RAISED)
        self.frame.pack(pady=25,padx=10,fill=tk.X)
        self.text = tk.Text(self.frame,height=5,width=50,fg="black",font="Times 15")
        self.text.pack(side=tk.LEFT,padx=10,pady=15)
        self.ebutton = tk.Button(self.frame,text="Encrypt",command=self.enc,font="Arial 20")
        self.ebutton.pack(padx=10,pady=70)

        # for decrypt
        self.frame = tk.Frame(master,width=650,height=200,bd=1,relief=tk.RAISED)
        self.frame.pack(pady=5,padx=10,fill=tk.X)
        self.etext = tk.Text(self.frame,height=5,width=50,fg="black",font="Times 15")
        self.etext.pack(side=tk.LEFT,padx=10,pady=15)
        self.dbutton = tk.Button(self.frame,text="Decrypt",command=self.dec,font="Arial 20")
        self.dbutton.pack(padx=10,pady=70)
    
    def enc(self):
        text = get(self.text)
        etext = Encryptor(text.upper())
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext)
    
    def dec(self):
        etext = get(self.etext)
        text = Decryptor(etext.lower())
        self.text.delete("1.0","end")
        self.text.insert(tk.END,text)

def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Atbash Cipher")
    #window.geometry("700x700")
    enc = Cipher(window)
    window.mainloop()