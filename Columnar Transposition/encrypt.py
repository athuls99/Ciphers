# Program to encrypt text into columnar tranposition cipher

# dependencies
from math import ceil

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

def decrypt(lkey,key):
    sortedkey = "".join(sorted(key))
    decText = "".join(list(map(lambda x: "".join(lkey[sortedkey.index(x)]),key)))
    return decText

# main
text = input("Enter the text: ")
text = text.replace(" ","")
key = input("Enter the key: ")
akey = arrange(text,list(key))
encText = encrypt(akey,key)
print(akey)
print("The encrypted text: ",encText)
dkey = darrange(encText,sorted(key))
print(dkey)
decText = decrypt(dkey,key)
print(decText)
    
