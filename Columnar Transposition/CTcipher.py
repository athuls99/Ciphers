# Program to encrypt text into columnar tranposition cipher

# dependencies
from math import ceil
from wordsegment import load,segment

# functions

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

# preprocess
load()

# main
text = input("Enter the text: ")
text = text.replace(" ","")
key = input("Enter the key: ")
akey = arrange(text,list(key))
encText = encrypt(akey,key)
print("The encrypted text: ",encText)
dkey = darrange(encText,sorted(key))
decText = decrypt(dkey,key,len(encText))
decText = segment(decText)
if "x" in decText[-1]:
    decText = decText[:-1]
print(" ".join(decText))
    
