#Atbash Cipher

"""
The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed.
"""

"""
We do not need a decyptor function seperately.
Encryption and decryption process both are the same in case of atbash cipher.

"""


def Encryptor(word):
    res=""
    for i in word:
        shift=0
        # Encrypt upper characters 
        if (i.isupper()):
            shift=25-(ord(i)-65)
            res+=chr(65+shift)
        # Encrypt lowercase characters 
        elif (i.islower()):
            shift=25-(ord(i)-97)
            res+=chr(97+shift)
        else:
            res+=i
    return res

def Decryptor(word):
    res=""
    return Encryptor(word)


word=input("Enter the word to be encrypted : ")
Enc=Encryptor(word)
print("Encrypted String is : ",Enc)
print("Decrypted string is : ",Decryptor(Enc))
