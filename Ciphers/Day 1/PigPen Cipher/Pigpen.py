#Pig Pen Cipher
import string

Encode = {'a' : '_|',
       'b' : '|_|',
       'c' : '|_',
       'd' : '=|',
       'e' : '|=|',
       'f' : '|=',
       'g' : '-|',
       'h' : '|-|',
       'i' : '|-',
       'j' : '_.|',
       'k' : '|._|',
       'l' : '|._',
       'm' : '=.|',
       'n' : '|.=|',
       'o' : '|.=',
       'p' : '-.|',
       'q' : '|.-|',
       'r' : '|.-',
       's' : '\\/',
       't' : '>',
       'u' : '<',
       'v' : '/\\',
       'w' : '\\./',
       'x' : '.>',
       'y' : '<.',
       'z' : '/.\\',
       ' ' : '   ',
       '{':'{',
       '}':'}',
       '$': '$',
       '(': '(',
       ',': ',',
       '0': '0',
       '1':'1',
       '2':'2',
       '3':'3',
       '4': '4',
       '5':'5',
       '6':'6',
       '7':'7',
       '8': '8',
       '9':'9',
       '@': '@',
       '|': '|',
       '#': '#',
       "'": "'",
       '+': '+',
       '/': '/',
       ';': ';',
       '?': '?',
       '[': '[',
       '_': '_',
       '&': '&',
       '*': '*',
       '.': '.',
       '!':'!',
       '-':'-',
       ':':':',
       ' ':' '}

Decode = dict(zip(Encode.values(),Encode.keys()))

"""
def input_Cleaner(word):
    word=word.replace('=','\=')
    word=word.replace('\\','\\\\')
    return word
"""

def Encryptor(msg):
    result = []
    msg = msg.lower()
    for _ in msg:
        result.append(Encode[_])
    return result

def Decryptor(msg_cipher):
    result = []
    for _ in msg_cipher:
        result.append(Decode[_])
    return ''.join(result)

print(" Enter your choice : \n 1.Encypt \n 2.Decrypt letter by letter \n 3.Decrypt entire string with space between each symbol")
ch=int(input())
if (ch==1):
    word=input("Enter the string to be Encrypted : ")
    enc_string=Encryptor(word)
    print("Encrypted string is : ",''.join(enc_string))
    #enc_string=input_Cleaner(enc_string)
    #print(enc_string)
elif (ch==2):
    ns=int(input("Enter the number of symbols : "))
    a=[]
    for i in range(ns):
        print("Enter symbol {} : ".format(i+1)) 
        a.append(input())
    dec_string=Decryptor(a)
    #print("Encrypted string is : ",''.join(enc_string))
    print("Decrypted string is : ",dec_string)
elif (ch==3):
    word=input("Enter string to be decrypted with $% in between each symbol : ")
    word=word.split("$%")
    dec_string=Decryptor(word)
    print("Decrypted string is : ",dec_string)
else:
    print("Invalid iput")
    




