from wordsegment import load,segment;
load();
def encrypt(text):
    text=text.upper()
    for i in text:
        if(ord(i)<65 or ord(i)>90):
            #print(i,ord(i))
            text = text.replace(i,"")
    text = text[::-1]
    print("THE ENCRYPTED TEXT IS")
    print(text)
def decrypt(text):
    text= text[::-1]
    text = segment(text)
    print("THE DECRYPTED TEXT IS")
    print((" ").join(text))
n=int(input("ENTER 0 TO ENCRYPT OR 1 TO DECRYPT\n"))
if(not n):
    text=input("ENTER THE PLAIN TEXT\n")
    encrypt(text)
else:
    text= input("ENTER THE ENCRYPTED TEXT\n")
    decrypt(text)
