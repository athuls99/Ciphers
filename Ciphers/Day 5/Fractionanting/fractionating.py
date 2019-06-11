def encrypt(text):
    dictt = {'a':'01','b':'02','c':'03','d':'04','e':'05','f':'06','g':'07','h':'08',
    'i':'09','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    arr=''
    new_text = text.lower()
    for i in list(new_text):
        for k, j in dictt.items():
            if k == i:
                arr+=j
    return arr

def decrypt(text):
    dictt = {'a':'01','b':'02','c':'03','d':'04','e':'05','f':'06','g':'07','h':'08',
    'i':'09','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    i=0
    arr=''
    while i<len(text):
        st=''
        st+=text[i]+text[i+1]
        for k,j in dictt.items():
            if j == st:
                arr+=k
        i+=2
    return arr

order=int(input("Choose :\n1,Encrypting \n2,Decrypting\n"))
if order==1:
    message=input("Please input the message (only from A-Z): ")
    print ("Cipher: ") 
    print (encrypt(message))
elif order==2:
    cipher=input("Please input the cipher text: ")
    print ("Plaintext:")
    print (decrypt(cipher))
else:
    print ("Error")
                
                
                
        
        
                

