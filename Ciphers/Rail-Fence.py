#Rail-Fence Cipher

"""
The rail fence cipher works by writing the message on alternate lines across the page, and then reading off each line in turn along a diagonal like fashion.
"""

def Encryptor(Word,key):
    res=""
    t=0
    while (len(res)!=len(Word)):
        for i in range(t,len(Word),(2*key)-2):
            res+=Word[i]
        t+=1
    return res



Word=input("Enter the word to be Encrypted")
key=int(input("Eter the key to be used"))
Res=Encryptor(Word,key)
print("The Encrypted string is : ",Res)
#print("The Decrypted string is : ",Decryptor(Res,key))
