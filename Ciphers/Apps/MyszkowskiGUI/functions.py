# dependencies
from collections import Counter
from math import ceil
from sympy import Matrix
from wordsegment import segment,load
import re

# preprocess
load()

# functions

def encrypt(text,key):
    keycount = Counter(key)
    encText = ""
    for i in sorted(set(key)):
        if keycount[i] == 1:
            ind = key.index(i)
            encText += "".join([chr(x) for x in text[:,ind]])
        else:
            start = 0
            li = []
            for k in range(keycount[i]):
                ind = key.index(i,start)
                j = [chr(x) for x in text[:,ind]]
                li.append(j)
                start = ind + 1
            for k in range(len(li[0])):
                for j in range(keycount[i]):
                    encText += li[j][k]                
    return encText



def createList(text,key):
    textlen = len(text)
    keylen = len(key)
    total = ceil(textlen/keylen)*keylen
    rem = total -textlen
    textlist = Matrix(int(total/keylen),keylen,[ord(x) for x in text] + [ord('X') for i in range(rem)])
    #textlist = Matrix(int(total/keylen),keylen,list(text) + ['X' for i in range(rem)])
    return textlist

def encryptText(text,key):
    text = re.sub(r'[^A-Za-z]',"",text)
    textlist = createList(text,key)
    encText = encrypt(textlist,key)
    return encText.upper()

def createFList(text,key):
    keycount = Counter(key)
    keylen = len(key)
    textlen = len(text)
    start = 0
    textlist = [list() for x in range(keylen)]
    no_of_rows = int(textlen/keylen)
    for i in sorted(set(key)):
        if keycount[i] == 1:
            ind = key.index(i)
            end = start + no_of_rows
            textlist[ind] = list(text[start:end])
            start = end
        else:
            indexes = []
            istart = 0
            count = keycount[i]
            for k in range(count):
                ind = key.index(i,istart)
                istart = ind + 1
                indexes.append(ind)
            end = start + (no_of_rows*count)
            part = text[start:end]
            s = start
            while(s<end):
                for j in indexes:
                    textlist[j].append(part[s-start])
                    s += 1
            start = end        
    return (textlist,no_of_rows)
            
def decrypt(text,key,r):
    decText = ""
    for i in range(r):
        for j in text:
            decText += j[i]
    return decText


def decryptText(text,key):
    (textlist,no_of_rows) = createFList(text,key)
    decText = decrypt(textlist,key,no_of_rows)
    decText = segment(decText)
    if "x" in decText[-1]:
        decText = decText[:-1]
    return " ".join(decText).lower()

def encryptor():
    text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    encText = encryptText(text.upper(),key)
    print("The encrypted text: ",encText)

def decryptor():
    text = input("Enter the Encrypted text: ")
    #text = re.sub(r'[^A-Za-z]',"",text)
    key =input("Enter the key: ")
    decText = decryptText(text,key)
    print("The Decrypted text: ",decText)
