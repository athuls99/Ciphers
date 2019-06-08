#Rail-Fence Cipher

"""
The rail fence cipher works by writing the message on alternate lines across the page, and then reading off each line in turn along a diagonal like fashion.
"""

def Encryptor(word,key):
    res=[[] for i in range(key)]
    length=[]
    eword=""
    kf=(2*key-1)
    for i in range(len(word)):
        res[i%key].append(i)
    print(res)
    for i in range(key):
        length.append(len(res[i]))
    s=min(length)
    for i in range(key):
        for j in range(s):
            eword+=word[res[i][j]]
    for i in range(key):
        if (len(res[i])==(s+1)):
            eword+=word[res[i][s]]
    return eword
        
                      
    
        
            



Word=input("Enter the word to be Encrypted")
key=int(input("Eter the key to be used"))
Res=Encryptor(Word,key)
print("The Encrypted string is : ",Res)
#print("The Decrypted string is : ",Decryptor(Res,key))
