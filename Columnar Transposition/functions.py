# dependencies
from time import time
from math import ceil
from wordsegment import load,segment
from itertools import permutations
from functools import reduce
from collections import Counter
import re
import ngrams

# preprocess
load()
fitness = ngrams.ngram_score('quadgrams.txt')
expectedvalues = {'a':0.082,'b':0.015,'c':0.028,'d':0.042,'e':0.127,'f':0.022,'g':0.020,
                 'h':0.061,'i':0.07,'j':0.002,'k':0.008,'l':0.040,'m':0.024,'n':0.068,
                 'o':0.075,'p':0.02,'q':0.001,'r':0.06,'s':0.063,'t':0.090,'u':0.028,
                 'v':0.01,'w':0.024,'x':0.002,'y':0.02,'z':0.001}


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

# Decryption without Key
def dArrange(text,keyLength):
    textLength = len(text)
    interval = textLength/keyLength
    textList = list(range(keyLength))
    j = 0 ; k = 0
    for i in range(textLength):
        if not j < interval:
            k += 1
            j = 1
        else:
            j += 1
        if type(textList[k]) is not list:
            textList[k] = []
        textList[k].append(text[i])
    return textList

def getWord(textList,ind):
    word = ""
    for i in range(len(textList)):
        word += textList[i][ind]
    return word

def getBestPerm(fWord,sWord,cRange):
    bestPerm = []
    perm = permutations(cRange)
    i = next(perm)
    limit = 5
    while True:
        word = ""
        for j in i:
            word += fWord[j]
        for j in i:
            word += sWord[j]
        ngramVal = fitness.score(word)
        print(word,ngramVal,i)
        if len(bestPerm) >= limit:
            remVal = min(bestPerm)            
            if ngramVal > remVal[0]:
                bestPerm.remove(remVal)
                bestPerm.append((ngramVal,i))
        else:
            bestPerm.append((ngramVal,i))
        try:
            i = next(perm)
        except:
            break
    print("bestperm:",bestPerm)
    return bestPerm

def getText(textList,perms):
    texts = []
    for j in perms:
        text = ""
        interval = len(textList[0])
        extraList = list(range(interval))
        #print(textList,perm,interval)
        perm = j[1]
        for i in perm:
            for j in range(interval):
                if type(extraList[j]) is not list:
                    extraList[j] = []
                extraList[j].append(textList[i][j])
                #print(extraList)
        for i in extraList:
            text += "".join(i)
        texts.append(text)
    return texts

def nkDecrpt(textList, perm):
    firstWord = getWord(textList,0)
    secondWord = getWord(textList,1)
    bestPerm = getBestPerm(firstWord,secondWord,perm)
    print(firstWord)
    text = getText(textList,bestPerm)
    return text


           
            

# exporting functions
def encryptText():
    text = input("Enter the text: ")
    text = re.sub(r'[^A-Za-z]',"",text)
    key = input("Enter the key: ")
    sTime = time()
    keyList = arrange(text,list(key))
    encryptedText = encrypt(keyList,key)
    print("The encrypted text: ", encryptedText)
    print("Total time:",time()-sTime)

def decryptText():
    text = input("Enter the encrypted text: ")
    key = input("Enter the key: ")
    sTime = time()
    keyList = darrange(text,list(key))
    decryptedText = decrypt(keyList,key,len(text))
    decryptedText = segment(decryptedText)
    if "x" in decryptedText[-1]:
        decryptedText = decryptedText[:-1]
    print("The decrypted text: "," ".join(decryptedText))
    print("Total time:",time()-sTime)
    

def nkDecryptText():
    text = input("Enter the encrypted text: ")
    sTime = time()
    textLength = len(text)
    maxRange = 11 if textLength > 11 else textLength
    decryptedText = ""
    for i in range(3,maxRange):
        if textLength % i == 0: 
            textList = dArrange(text,i)
            #perm = list(permutations(list(range(i))))
            decryptedText = nkDecrpt(textList,list(range(i)))
            dtextlist = []
            for dText in decryptedText:
                ngramVal = fitness.score(dText)
                print(dText,ngramVal,i)
                dtextlist.append((ngramVal,dText))
            bestSet = max(dtextlist)
            print("Is this the decryted text:",bestSet[1])
            confirm = int(input("1.YES\n2.NO\n"))
            if confirm == 1:
                decryptedText = bestSet[1]
                break
    if len(decryptedText) > 0:
        #print(decryptedText)
        decryptedText = segment(decryptedText)
        if "x" in decryptedText[-1]:
            decryptedText = decryptedText[:-1]
        print("The decrypted text: "," ".join(decryptedText))
    else:
        print("Not Found")
    print("Total time:",time()-sTime)
   

