import tkinter as tk
import turtle

class Cipher:
    def __init__(self,master):
        self.frame = tk.Frame(master)
        self.frame.pack(expand=1,pady=25,padx=10,fill=tk.X)

        # for encrypt
        self.text = tk.Text(self.frame,height=5,width=50,fg="black",font="Times 15")
        self.text.pack(side=tk.LEFT,padx=10,pady=15)
        self.ebutton = tk.Button(self.frame,text="Encrypt",command=self.enc,font="Arial 20")
        self.ebutton.pack(padx=10,pady=70)

window = tk.Tk()
window.geometry("800x800")
cipher = Cipher(window)
window.mainloop()