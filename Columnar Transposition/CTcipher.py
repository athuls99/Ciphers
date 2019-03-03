# Program to encrypt text into columnar tranposition cipher

# dependencies
from wordsegment import load,segment
from functions import *

# preprocess
load()

# interface functions
def encryptText():
    text = input("Enter the text: ")
    text = text.replace(" ","")
    key = input("Enter the key: ")
    keyList = arrange(text,list(key))
    encryptedText = encrypt(keyList,key)
    print("The encrypted text: ", encryptedText)

def decryptText():
    text = input("Enter the encrypted text: ")
    text = text.replace(" ","")
    key = input("Enter the key: ")
    keyList = darrange(text,list(key))
    decryptedText = decrypt(keyList,key,len(text))
    decryptedText = segment(decryptedText)
    if "x" in decryptedText[-1]:
        decryptedText = decryptedText[:-1]
    print("The decrypted text: "," ".join(decryptedText))

# main
if __name__ == "__main__":
    n = int(input("1.Encrypt\n2.Decrypt with key\n3.Decrypt without key\n"))
    if n == 1:
        encryptText()
    elif n == 2:
        decryptText()
    
    
