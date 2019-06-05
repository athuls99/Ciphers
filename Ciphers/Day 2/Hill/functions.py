from sympy import Matrix
import math
import re

def isPerfect(n):
    root = math.sqrt(n)
    if(root - math.floor(root)) == 0:
        return True
    return False

def createMatrix(text,order,opt):
    if opt == 0:
        Mat = Matrix(order,order,[ord(char)-97 for char in text])
    elif opt == 1:
        textL = len(text)
        rows = math.ceil(textL/order)
        totalLen = rows*order
        Mat = Matrix(rows,order,[ord(char)-97 for char in text]+['x' for x in range(totalLen - textL)])
    return Mat  

def checkKey(n):
    if math.gcd(n,26) == 1:
        return True
    return False

def crypt(tMat,kMat,order):
    rows = tMat.rows
    encMat = Matrix()
    for i in range(rows):
        encRow = kMat*(tMat[i,:].transpose())
        encMat = Matrix([encMat,[char%26 for char in encRow]])
    text = "".join([chr(val+97) for val in encMat])
    return text

def encryptText(text,key):
    lKey = len(key)
    if isPerfect(lKey):
        order = int(lKey**(1/2))
        keyMat = createMatrix(key,order,0)
        det = keyMat.det()
        if checkKey(det):
            textMat = createMatrix(text,order,1)
            encText = crypt(textMat,keyMat,order)
            print("The encrypted text is: ",encText)
        else:
            print("The key is not Invertible!!")
    else:
        print("The length of key should be Perfect Square!!")

def encryptor():
    inpText = input("Enter the Text: ")
    inpText = re.sub(r'[^A-Za-z]',"",inpText)
    key = input("Enter the key: ")
    encryptText(inpText.lower(),key.lower())