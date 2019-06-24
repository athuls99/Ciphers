from FreqFInal import getFrequency,decrypt
import tkinter as tk
from tkinter import ttk

class Cipher:
    def __init__(self,master):
        self.master = master

        self.oframe = tk.Frame(master)
        self.oframe.pack(expand=1,pady=5,padx=5)
        # for encrypt
        self.frame = tk.Frame(self.oframe,bd=1,relief=tk.RAISED)
        self.frame.pack(expand=1,side=tk.LEFT,pady=5,padx=10)
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1)
        label = tk.Label(iframe,text="Plain text",font="Times 20 bold")
        label.pack(padx=10)
        self.ebutton = tk.Button(iframe,text="Decrypt",command=self.enc,font="Arial 15")
        self.ebutton.pack(side=tk.LEFT,padx=10)
        self.ebutton = tk.Button(iframe,text="Clear",command=lambda: self.clear(0),font="Arial 15")
        self.ebutton.pack(padx=10)
        self.text = tk.Text(self.frame,height=25,width=70,fg="black",font="Times 15")
        self.text.pack(padx=10,pady=2)
        

        # for decrypt
        self.frame = tk.Frame(self.oframe,bd=1,relief=tk.RAISED)
        self.frame.pack(expand=1,pady=5,padx=10,fill=tk.X)
        eframe = tk.Frame(self.frame)
        eframe.pack(expand=1)
        label = tk.Label(eframe,text="Cipher text",font="Times 20 bold")
        label.pack(padx=10)
        self.dbutton = tk.Button(eframe,text="Clear",command=lambda: self.clear(1),font="Arial 15")
        self.dbutton.pack(padx=10)
        self.etext = tk.Text(self.frame,height=25,width=70,fg="black",font="Times 15")
        self.etext.pack(padx=10,pady=2)        
    
    def enc(self):
        text = get(self.text)
        freqarr = getFrequency(text)
        self.print_freq(freqarr)
        etext = decrypt(text,freqarr)
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext.upper())

    def clear(self,opt):
        if opt == 0:
            self.text.delete("1.0","end")
        else:
            self.etext.delete("1.0","end")

    def print_freq(self,freq):
        freqalpha = "ETAOINSRHDLUCMFYWGPBVKXQJZ"
        frame = tk.Frame(self.master,bd=1,relief=tk.RAISED)
        frame.pack(expand=1,pady=5,padx=10,fill=tk.X)
        j = 0
        for i in freq:
            iframe = tk.Frame(frame)
            iframe.pack(side=tk.LEFT,padx=1,pady=1)
            label1 = tk.Label(iframe,text=i[0],bd=2,relief=tk.SUNKEN,width=6,font="Times 11",bg='white')
            label1.pack(pady=1)         # display letter
            label2 = tk.Label(iframe,text=i[2],bd=2,relief=tk.SUNKEN,width=6,font="Times 11",bg='white')
            label2.pack(pady=1)         # display the no. of occurrences
            label3 = tk.Label(iframe,text=i[1],bd=2,relief=tk.SUNKEN,width=6,font="Times 11",bg='white')
            label3.pack(pady=1)         # display frequency
            label4 = tk.Label(iframe,text=freqalpha[j],bd=2,relief=tk.SUNKEN,width=6,font="Times 11",bg='white')
            label4.pack(pady=1)         # display the substitute letter
            j += 1



def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Frequency Analysis Cipher")
    #window.geometry("700x700")
    enc = Cipher(window)
    window.mainloop()