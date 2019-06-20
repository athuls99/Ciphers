from wordsegment import load,segment
load()
def encrypt(text):
    text=text.upper()
    for i in text:
        if(ord(i)<65 or ord(i)>90):
            #print(i,ord(i))
            text = text.replace(i,"")
    text = text[::-1]
    return text
    
def decrypt(text):
    text= text[::-1]
    text = segment(text)
    return (" ").join(text)

if __name__ == "__main__":    
    n=int(input("ENTER 0 TO ENCRYPT OR 1 TO DECRYPT\n"))
    if(not n):
        text=input("ENTER THE PLAIN TEXT\n")
        text = encrypt(text)
        print("THE ENCRYPTED TEXT IS")
        print(text)
        
    else:
        text= input("ENTER THE ENCRYPTED TEXT\n")
        dtext = decrypt(text)
        print("THE DECRYPTED TEXT IS: ")
        print(dtext)
