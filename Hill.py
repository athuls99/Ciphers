from sympy import Matrix
import numpy as np

def Encryptor(plain_text,keyw):
    l=len(plain_text)
    n=l**2
    t=len(keyw)
    k=0
    key=keyw.upper()
    new_text=plain_text.upper()
    b=[[] for i in range(l)]
    a=[[] for i in range(l)]
    for i in range(l):
        for j in range(l):
            a[i].append((ord(key[k])-65)%26)
            k=(k+1)%t
    #print(a)
    for i in range(l):
        b[i].append((ord(new_text[i])-65)%26)
    #print(b)   
    m=np.matmul(a,b)
    enc_string=""
    #print(m)
    for i in range(l):
        enc_string+=chr(65+(m[i][0])%26)
    return enc_string

def Decryptor(Encrypted_string,keyw):
    l=len(Encrypted_string)
    n=l**2
    t=len(keyw)
    k=0
    dec_string=""
    key=keyw.upper()
    new_text=Encrypted_string.upper()
    b=[[] for i in range(l)]
    a=[[] for i in range(l)]
    for i in range(l):
        for j in range(l):
            a[i].append((ord(key[k])-65)%26)
            k=(k+1)%t
    #print(a)
    At=Matrix(a)
    #ai=np.linalg.inv(a)
    ata=At.inv_mod(26)
    #p=list(ata)
    #print(ai)
    #print(ata)
    for i in range(l):
        b[i].append((ord(new_text[i])-65)%26)
    #print(b)
    b=Matrix(b)
    #m=np.matmul(ai,b)
    #p=np.concatenate(ata).astype(None)
    m=ata*b
    kl=np.array(m).astype(np.int)
    #print(kl)
    
    for i in range(l):
        dec_string+=chr(65+((kl[i][0])%26))
    return dec_string
    
    
    
    
            
plain_text=input("Enter the Text to be encrypted:")
Key_word=input("Enter the Key to be used:")
Encrypted_string=Encryptor(plain_text,Key_word)
try :
    Decrypted_string=Decryptor(Encrypted_string,Key_word)
except:
    Decrypted_string=""
    
print("Encrypted String:",Encrypted_string)
print("Decrypted String:",Decrypted_string)


            
            
    
                
    
