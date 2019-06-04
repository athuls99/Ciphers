#Pig Pen Cipher

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

word=input("Enter the string to be Encrypted : ")
enc_string=Encryptor(word)
#enc_string=input_Cleaner(enc_string)
#print(enc_string)
dec_string=Decryptor(enc_string)
print("Encrypted string is : ",''.join(enc_string))
print("Decrypted string is : ",dec_string)




