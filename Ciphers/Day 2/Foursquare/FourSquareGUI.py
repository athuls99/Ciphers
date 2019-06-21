from foursqaure import encrypt,decrypt,gen_matrix,get_key
import tkinter as tk
from tkinter import ttk
from wordsegment import load,segment
import re

class Start:
    def __init__(self,master):
        self.frame = tk.Frame(master,width=700,height=200)
        self.frame.pack(pady=1,padx=10)
        labelA = tk.Label(self.frame,text="Key 1 ",fg="black",font="Arial 15")
        self.a = tk.Text(self.frame,height=1,width=15,font="Times 15")
        labelA.pack(side=tk.LEFT,padx=5)
        self.a.pack(side=tk.LEFT,padx=1)
        labelB = tk.Label(self.frame,text="Key 2 ",fg="black",font="Arial 15")
        self.b = tk.Text(self.frame,height=1,width=15,font="Times 15")
        labelB.pack(side=tk.LEFT,padx=5)
        self.b.pack(side=tk.LEFT,padx=1)

class Cipher:
    def __init__(self,master,obj):
        self.k1 = obj.a
        self.k2 = obj.b

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
        self.text = tk.Text(self.frame,height=40,width=50,fg="black",font="Times 15")
        self.text.pack(padx=10,pady=1)

        # for the squares
        self.frame = tk.Frame(master,width=650)
        self.frame.pack(side=tk.LEFT,pady=1,padx=10,fill=tk.X)
        # first row
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1,padx=10,fill=tk.X)
        self.topLeft = tk.Text(iframe,height=5,width=11,fg="black",font="Times 15")
        self.topLeft.pack(side=tk.LEFT,padx=5,pady=10)
        self.topRight = tk.Text(iframe,height=5,width=11,fg="black",font="Times 15")
        self.topRight.pack(side=tk.LEFT,padx=5,pady=10)
        # second row
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1,padx=10,fill=tk.X)
        self.botLeft = tk.Text(iframe,height=5,width=11,fg="black",font="Times 15")
        self.botLeft.pack(side=tk.LEFT,padx=5,pady=10)
        self.botRight = tk.Text(iframe,height=5,width=11,fg="black",font="Times 15")
        self.botRight.pack(side=tk.LEFT,padx=5,pady=10)


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
        self.etext = tk.Text(self.frame,height=40,width=50,fg="black",font="Times 15")
        self.etext.pack(padx=10,pady=1)
    
    def enc(self):
        text = get(self.text).upper()
        text = re.sub(r'[^A-Za-z]',"",text)
        key1 = get(self.k1).upper()
        key2 = get(self.k2).upper()
        self.sett(text,key1,key2)
        etext = encrypt(text,key1,key2)
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext)
    
    def dec(self):
        etext = get(self.etext).upper()
        etext = re.sub(r'[^A-Za-z]',"",etext)
        key1 = get(self.k1).upper()
        key2 = get(self.k2).upper()
        self.sett(etext,key1,key2)
        text = decrypt(etext,key1,key2)
        text = segment(text)
        if 'x' in text[-1] and len(text[-1]) == 1:
            text = text[:-1]
        self.text.delete("1.0","end")
        self.text.insert(tk.END," ".join(text).lower())

    def clear(self,opt):
        if opt == 0:
            self.text.delete("1.0","end")
        else:
            self.etext.delete("1.0","end")
    
    def sett(self,text,key1,key2):
        char = ('J','j')
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
        if (char[0] not in key1) and ( char[0] not in key2) and (char[1] not in text): 
            alphabet.remove(char[1])
            alpha.remove(char[0])
        else:
            alphabet.remove('i')
            alpha.remove('I')
        # plaintext matrices
        mat1 = gen_matrix(alphabet)
        self.topLeft.delete("1.0","end")
        self.botRight.delete("1.0","end")
        self.printMat(mat1,0)
        # key 1 matrix
        mat2 = get_key(key1,alpha)
        mat2 = gen_matrix(mat2)
        self.topRight.delete("1.0","end")
        self.printMat(mat2,1)
        # key 2 matrix
        mat3 = get_key(key2,alpha)
        mat3 = gen_matrix(mat3)
        self.botLeft.delete("1.0","end")
        self.printMat(mat3,2)


    
    def printMat(self,mat,opt):
        for counter in range(5):
            put = mat[counter][0] + ' ' + mat[counter][1] + ' ' + mat[counter][2] + ' ' + mat[counter][3] + ' ' + mat[counter][4] + '\n'
            if opt == 0:
                self.topLeft.insert(tk.END,put)
                self.botRight.insert(tk.END,put)
            elif opt == 1:
                self.topRight.insert(tk.END,put)
            else:
                self.botLeft.insert(tk.END,put)

def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    load()
    window = tk.Tk()
    window.title("FourSquare Cipher")
    #window.geometry("700x700")
    sobj = Start(window)
    enc = Cipher(window,sobj)
    window.mainloop()
