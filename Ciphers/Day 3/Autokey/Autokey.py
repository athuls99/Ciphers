"""
Autokey Cipher is a polyalphabetic substitution cipher.
It is similar to Vigenere cipher except for the fact that the key doesn't repeat but the key is extended to the length of the plaintext by using the plaintext itself.
"""
def gen_key(word):
    key=input("Enter the key to be used : ")
    nkey=""
    if (len(key)==len(word)):
        return key
    elif (len(key)>len(word)):
        return key[0:len(word)]
    else:
        nkey=key+word[0:(len(word)-len(key))]
    return nkey

def d_gen_key(word):
    key=input("Enter the key to be used : ")
    nkey=""
    alphabet="".join([chr(i) for i in range(65,92)])
    if (len(key)==len(word)):
        return key
    elif (len(key)>len(word)):
        return key[0:len(word)]
    else:
        
    return nkey
    
    
def Encryptor(word):
    key=gen_key(word)
    key=key.upper()
    word=word.upper()
    l=len(key)
    eword=""
    for i in range(l):
        eword+=chr((ord(key[i])+ord(word[i])-130)%26+65)
    return eword

def Decryptor(word):
    key=gen_key(word)
    key=key.upper()
    word=word.upper()
    l=len(key)
    print(key)
    dword=""
    temp=0
    for i in range(l):
        temp=ord(word[i])-ord(key[i])
        #dword+=chr((temp+26)%26+65)
        
        if (temp>=0):
            dword+=chr(temp+65)
        else:
            dword+=chr(91+temp)
    return dword
    

        
    
    


print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
ch=int(input("Enter your choice : "))
while (ch):
    if (ch==1):
        word=input("Enter the word to be encypted using Autokey Cipher : ")
        print("Encrypted String is : ",Encryptor(word))
    elif (ch==2):
        word=input("Enter the word to be decypted using Autokey Cipher : ")
        print("Decrypted String is : ",Decryptor(word))
    print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
    ch=int(input("Enter your choice : "))
    
        

