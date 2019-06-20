def encrypt(text):
    text=text.upper()
    for i in text:
        if(ord(i) != 32 and (ord(i)<65 or ord(i)>90) ):
            
            text = text.replace(i,"")
    
    wordArr = text.split(" ")
    for i in range(len(wordArr)):
        wordArr[i] = wordArr[i][::-1]
    entext=(" ").join(wordArr)
    return entext
    

def decrypt(text):
    wordArr = text.split(" ")
    for i in range(len(wordArr)):
        wordArr[i] = wordArr[i][::-1]
    entext=(" ").join(wordArr)
    return entext
    

if __name__ == "__main__":
    n=int(input("ENTER 0 TO ENCRYPT OR 1 TO DECRYPT\n"))
    if(not n):
        text=input("ENTER THE PLAIN TEXT\n")
        entext = encrypt(text)
        print("THE ENCRYPTED TEXT IS")
        print(entext)
    else:
        text= input("ENTER THE ENCRYPTED TEXT\n")
        entext = decrypt(text)
        print("THE DECRYPTED TEXT IS")
        print(entext)
