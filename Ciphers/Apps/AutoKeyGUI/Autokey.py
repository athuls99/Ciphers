"""
Autokey Cipher is a polyalphabetic substitution cipher.
It is similar to Vigenere cipher except for the fact that the key doesn't repeat but the key is extended to the length of the plaintext by using the plaintext itself.
"""
def gen_key(word,key):
    #key=input("Enter the key to be used : ")
    nkey=""
    if (len(key)==len(word)):
        return key
    elif (len(key)>len(word)):
        return key[0:len(word)]
    else:
        nkey=key+word[0:(len(word)-len(key))]
    return nkey
     
def Encryptor(word,key):
    word=word.replace(" ","")
    key=gen_key(word,key)
    key=key.upper()
    word=word.upper()
    l=len(key)
    eword=""
    for i in range(l):
        eword+=chr((ord(key[i])+ord(word[i])-130)%26+65)
    return eword

def Decryptor(word,key):
    #key=gen_key(word)
    #key=input("Enter the key to be used : ")
    key=key.upper()
    word=word.upper()
    word=word.replace(" ","")
    w=len(word)
    #print(key)
    dword=""
    temp=0
    for i in range(w):
        temp=ord(word[i])-ord(key[i])
        #dword+=chr((temp+26)%26+65)
        if (temp>=0):
            dword+=chr(temp+65)
        else:
            dword+=chr(91+temp)
        if (len(key)<len(word)):
            key+=dword[i]
    return dword.lower()
if __name__ == "__main__":
    print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
    ch=int(input("Enter your choice : "))
    while (ch):
        if (ch==1):
            word=input("Enter the word to be encypted using Autokey Cipher : ")
            key=input("Enter the key to be used : ")
            print("Encrypted String is : ",Encryptor(word,key))
        elif (ch==2):
            word=input("Enter the word to be decypted using Autokey Cipher : ")
            print("Decrypted String is : ",Decryptor(word,key))
        print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
        ch=int(input("Enter your choice : "))
    
        

