from sympy import Matrix
import math
import re
import inspect

def isPerfect(n):
    root = math.sqrt(n)
    if(root - math.floor(root)) == 0:
        return True
    return False

def createMatrix(text,order,opt):
    if opt == 0:
        Mat = Matrix(order,order,[ord(char)-65 for char in text])
    elif opt == 1:
        textL = len(text)
        rows = math.ceil(textL/order)
        totalLen = rows*order
        Mat = Matrix(rows,order,[ord(char)-65 for char in text]+[ord('X')-65 for x in range(totalLen - textL)])
    return Mat  

def checkKey(n):
    if math.gcd(n,26) == 1:
        return True
    return False

def getMod(det):
    for i in range(1,26):
        if (i*det)%26 == 1:
            return i


def getInverse(key,det):
    det = int(det%26)
    dInv = getMod(det)
    nkey = dInv*(key.adjugate())
    return nkey

def crypt(tMat,kMat,order):
    rows = tMat.rows
    encMat = Matrix()
    for i in range(rows):
        encRow = kMat*(tMat[i,:].transpose())
        encMat = Matrix([encMat,[char%26 for char in encRow]])
    text = "".join([chr(val+65) for val in encMat])
    return text

def textEncDec(text,key,opt):
    lKey = len(key)
    if isPerfect(lKey):
        order = int(lKey**(1/2))
        keyMat = createMatrix(key,order,0)
        det = keyMat.det()
        if checkKey(det):
            text = re.sub(r'[^A-Za-z]',"",text)
            textMat = createMatrix(text,order,1)
            if opt == 0:
                encText = crypt(textMat,keyMat,order)
                return encText
            elif opt == 1:
                newKey = getInverse(keyMat,det)
                decText = crypt(textMat,newKey,order)
                return decText.lower()
        else:
            print("The key is not Invertible!!")
    else:
        print("The length of key should be Perfect Square!!")

def encryptor():
    inpText = input("Enter the Text: ").upper()
    key = input("Enter the key: ").upper()
    etext = textEncDec(inpText.upper(),key.upper(),0)
    print("The encrypted text is: ",etext)

def decryptor():
    text = input("Enter the Encrypted Text: ").upper()
    key = input("Enter the key: ").upper()
    dtext = textEncDec(text,key,1)
    print("The decrypted text is: ",dtext)
