
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
            echar=97+(ord(i)+ord(key[j]))%26
        enc_string+=chr(echar)
        j=(j+1)%l
    return enc_string
        
        
        
plaintext=input("Enter the text to be encrypted:")
keyword=input("Enter the Key:")
print("Encrypted String is:",Encryptor(plaintext,keyword))
