
import re

def occ_finder(word,sentence):
    k=[]
    for match in re.finditer(word, sentence):
        k.append(match.start(), match.end())
    return k


def find_key(word):
        


def Decryptor(word):
    


print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
ch=int(input("Enter your choice : "))
while (ch):
    word=input("Enter the word to be decypted using Vigenere Cipher : ")
    print("Decrypted String is : ",Decryptor(word))
    print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
    ch=int(input("Enter your choice : "))