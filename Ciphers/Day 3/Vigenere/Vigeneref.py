

def Encryptor(plain_t,key):
    l=len(key)
    j=0
    enc_string=""
    echar=0
    for i in plain_t:
        if (i.isupper() and key[j].isupper()):
            echar=65+(ord(i)+ord(key[j]))%26
        elif (i.islower() and key[j].islower()):
            echar=97+((ord(i)+ord(key[j]))%26)
        enc_string+=chr(echar)
        j=(j+1)%l
    return enc_string.upper()

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
    
def Decryptor(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))

if __name__ == "__main__":
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