
import tkinter as tk
from tkinter import ttk

freqalpha = "ETAOINSRHDLUCMFYWGPBVKXQJZ"


def getFrequency(encryptedText):
    frequencyArray = []

    for i in range(0, ord('Z') - ord('A') + 1):
        tempChar = chr(ord('A') + i)
        c = encryptedText.count(tempChar)
        temp = float("%.2f" % (float(c) / len(encryptedText) * 100))
        frequencyArray.append(
            [tempChar, temp, c])

    frequencyArray.sort(key=lambda x: x[2] - (0.0001*ord(x[0])))
    frequencyArray.reverse()
    return frequencyArray


def decrypt(encryptedText, frequencyArray):
    lenAplha = len(freqalpha)
    lenText = len(encryptedText)

    replacementPairs = []

    for i in range(lenAplha):
        replacementPairs.append((frequencyArray[i][0], freqalpha[i]))

    decryptArr = []
    print(replacementPairs)
    for i in encryptedText:
        decryptArr.append(i)

    for i in replacementPairs:
        for j in range(lenText):
            if(decryptArr[j] == i[0]):
                decryptArr[j] = i[1].lower()
    decryptedText = ("").join(decryptArr)
    return decryptedText


class Cipher:
    def __init__(self, master):
        self.master = master

        self.oframe = tk.Frame(master)
        self.oframe.pack(expand=1, pady=5, padx=5)
        # for encrypt
        self.frame = tk.Frame(self.oframe, bd=1, relief=tk.RAISED)
        self.frame.pack(expand=1, side=tk.LEFT, pady=5, padx=10)
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1)
        label = tk.Label(iframe, text="Cipher Text", font="Times 20 bold")
        label.pack(padx=10)
        self.ebutton = tk.Button(
            iframe, text="Decrypt", command=self.enc, font="Arial 15")
        self.ebutton.pack(side=tk.LEFT, padx=10)
        self.ebutton = tk.Button(
            iframe, text="Clear", command=lambda: self.clear(0), font="Arial 15")
        self.ebutton.pack(padx=10)
        self.text = tk.Text(self.frame, height=20, width=65,
                            fg="black", font="Times 15")
        self.text.pack(padx=10, pady=2)

        # for decrypt
        self.frame = tk.Frame(self.oframe, bd=1, relief=tk.RAISED)
        self.frame.pack(expand=1, pady=5, padx=10, fill=tk.X)
        eframe = tk.Frame(self.frame)
        eframe.pack(expand=1)
        label = tk.Label(eframe, text="Decrypted Text", font="Times 20 bold")
        label.pack(padx=10)
        self.dbutton = tk.Button(
            eframe, text="Clear", command=lambda: self.clear(1), font="Arial 15")
        self.dbutton.pack(padx=10)
        self.etext = tk.Text(self.frame, height=20,
                             width=65, fg="black", font="Times 15")
        self.etext.pack(padx=10, pady=2)

    def enc(self):
        text = get(self.text).upper()
        print(type(text))
        freqarr = getFrequency(text)
        self.print_freq(freqarr)
        etext = decrypt(text, freqarr)
        self.etext.delete("1.0", "end")
        self.etext.insert(tk.END, etext.lower())

    def clear(self, opt):
        if opt == 0:
            self.text.delete("1.0", "end")
        else:
            self.etext.delete("1.0", "end")

    def print_freq(self, freq):
        freqalpha = "ETAOINSRHDLUCMFYWGPBVKXQJZ"
        frame = tk.Frame(self.master, bd=1, relief=tk.RAISED)
        frame.pack(expand=1, pady=5, padx=10, fill=tk.X)
        j = 0
        for i in freq:
            iframe = tk.Frame(frame)
            iframe.pack(side=tk.LEFT, padx=1, pady=1)
            label1 = tk.Label(
                iframe, text=i[0], bd=2, relief=tk.SUNKEN, width=6, font="Times 11", bg='white')
            label1.pack(pady=1)         # display letter
            label2 = tk.Label(
                iframe, text=i[2], bd=2, relief=tk.SUNKEN, width=6, font="Times 11", bg='white')
            label2.pack(pady=1)         # display the no. of occurrences
            label3 = tk.Label(
                iframe, text=i[1], bd=2, relief=tk.SUNKEN, width=6, font="Times 11", bg='white')
            label3.pack(pady=1)         # display frequency
            label4 = tk.Label(
                iframe, text=freqalpha[j], bd=2, relief=tk.SUNKEN, width=6, font="Times 11", bg='white')
            label4.pack(pady=1)         # display the substitute letter
            j += 1


def get(obj):
    return obj.get("1.0", "end").strip()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Frequency Analysis Cipher")
    # window.geometry("700x700")
    enc = Cipher(window)
    window.mainloop()
