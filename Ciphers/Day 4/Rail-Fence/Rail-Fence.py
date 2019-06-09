#Rail-Fence Cipher

"""
The rail fence cipher works by writing the message on alternate lines across the page, and then reading off each line in turn along a diagonal like fashion.
"""

def Encryptor(word,key):
    down=0
    Rf=[[-1 for i in range(len(word))]for j in range(key)]
    print(Rf)
    c=0
    r=0
    for i in range(len(word)):
        if (r==0) or (r==(key-1)):
            down=not down
        Rf[r][c]=word[i]
        c+=1
        if (down==1):
            r+=1
        else:
            r-=1
    print(Rf)
    elist = [] 
    for i in range(key): 
        for j in range(len(word)): 
            if Rf[i][j] != -1: 
                elist.append(Rf[i][j])
    return "".join(elist)

def get_Rail_Matrix(word,key):
    down=0
    Rf=[['_' for i in range(len(word))]for j in range(key)]
    #print(Rf)
    c=0
    r=0
    for i in range(len(word)):
        if (r==0) or (r==(key-1)):
            down=not down
        Rf[r][c]='$'
        c+=1
        if (down==1):
            r+=1
        else:
            r-=1
    return Rf
    
def Decryptor(ciphertext,key):
    RM=get_Rail_Matrix(ciphertext,key)
    k=0
    for i in range(key):
        for j in range(len(ciphertext)):
            if (RM[i][j]=='$') and (k<len(ciphertext)):
                RM[i][j]=ciphertext[k]
                k+=1
    r,c=0,0
    down=0
    dlist=[]
    for i in range(len(ciphertext)): 
        if (r==0) or (r==(key-1)):
            down=not down
        if (RM[r][c] != '$'): 
            dlist.append(RM[r][c]) 
            c += 1
        if down: 
            r += 1
        else: 
            r-= 1
    return("".join(dlist)) 
    
    

Word=input("Enter the word to be Encrypted : ")
key=int(input("Eter the key to be used : "))
Res=Encryptor(Word,key)
print("The Encrypted string is : ",Res)
print("The Decrypted string is : ",Decryptor(Res,key))
