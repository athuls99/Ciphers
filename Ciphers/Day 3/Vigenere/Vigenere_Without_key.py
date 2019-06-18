
#Assuming the Key as well as the plaintext are of the same case

def Encryptor(plain_t,key):
    l=len(key)
    j=0
    k=0
    enc_string=""
    echar=0
    for i in plain_t:
        if (i.isupper() and key[j].isupper()):
            echar=65+(ord(i)+ord(key[j]))%26
        elif (i.islower() and key[j].islower()):
            echar=97+((ord(i)+ord(key[j]))%26)
        enc_string+=chr(echar)
        j=(j+1)%l
    return enc_string

def Decryptor(Encrypted_string,key):
    l=len(key)
    j=0
    dec_string=""
    dchar=0
    for i in Encrypted_string:
        if (i.isupper() and key[j].isupper()):
            dchar=65+(ord(i)-ord(key[j])+26)%26
        elif (i.islower() and key[j].islower()):
            dchar=97+((ord(i)-ord(key[j])+26)%26)
        dec_string+=chr(dchar)
        j=(j+1)%l
    return dec_string


"""      
plaintext=input("Enter the text to be encrypted:")
keyword=input("Enter the Key:")
Encrypted_string=Encryptor(plaintext,keyword)
Decrypted_string=Decryptor(Encrypted_string,keyword)
print("Encrypted String is:",Encrypted_string)
print("Decrypted String is:",Decrypted_string)
"""
def Vigenere_Without_key(ciphertext):
    #Quadgrams
    
    return 1

print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
ch=int(input("Enter your choice : "))
while (ch):
    if (ch==1):
        word=input("Enter the word to be encypted using Vigenere Cipher : ")
        keyword=input("Enter the Key:")
        print("Encrypted String is : ",Encryptor(word,keyword))
    elif (ch==2):
        word=input("Enter the word to be decypted using Vigenere Cipher : ")
        keyword=input("Enter the Key:")
        print("Decrypted String is : ",Decryptor(word,keyword))
    print(" 1.Encrypt\n 2.Decrypt\n 0.Exit")
    ch=int(input("Enter your choice : "))
