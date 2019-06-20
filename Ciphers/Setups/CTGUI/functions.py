# dependencies
from time import time
from math import ceil
from wordsegment import load,segment
from functools import reduce
from collections import Counter
import re


# preprocess
load()


# functions

# Encryption
def arrange(text,key):
    lText = len(text)
    lKey = len(key)
    total = ceil(lText/lKey)*lKey
    text = text + (total - lText)*"x"
    for i in range(total):
        j = i%lKey
        if type(key[j]) is not list: 
            key[j] = []
        key[j].append(text[i])
    return key

def encrypt(lkey,key):
    sortedkey = "".join(sorted(key))
    encText = "".join(list(map(lambda x: "".join(lkey[key.index(x)]),sortedkey)))
    return encText 

# Decryption with Key
def darrange(text,key):
    lText = len(text)
    lKey = len(key)
    interval = lText/lKey
    j = 0
    k = 0
    for i in range(lText):
        if not j < interval:
            k += 1
            j = 1
        else:
            j += 1
        if type(key[k]) is not list: 
            key[k] = []
        key[k].append(text[i])
    return key

def decrypt(lkey,key,tLen):
    sortedkey = "".join(sorted(key))
    text = "".join(list(map(lambda x: "".join(lkey[sortedkey.index(x)]),key)))
    kLen = len(key)
    interval = int(tLen/kLen)
    decText = ""
    k = 1
    for i in range(interval):
        j = i
        while j<tLen:
            decText += text[j]
            j = i + interval * k
            k += 1
        k = 1
    return decText
           
            

# exporting functions
def encryptText(text,key):
    text = re.sub(r'[^A-Za-z]',"",text)
    keyList = arrange(text,list(key))
    encryptedText = encrypt(keyList,key)
    return encryptedText.upper()

def encryptor():
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    sTime = time()
    encryptedText = encryptText(text,key)
    print("The encrypted text: ", encryptedText)
    print("Total time:",time()-sTime)

def decryptText(text,key):
    keyList = darrange(text,list(key))
    decryptedText = decrypt(keyList,key,len(text))
    decryptedText = segment(decryptedText)
    if "x" in decryptedText[-1]:
        decryptedText = decryptedText[:-1]
    return " ".join(decryptedText).lower()
    
def decryptor():
    text = input("Enter the encrypted text: ")
    key = input("Enter the key: ")
    sTime = time()
    decryptedText = decryptText(text,key)
    print("The decrypted text: ",decryptedText)
    print("Total time:",time()-sTime)


