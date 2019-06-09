# Program to encrypt text into columnar tranposition cipher

# dependencies
from functions import encryptText,decryptText

# main
if __name__ == "__main__":
    while True:
        print("1.Encrypt\n2.Decrypt with key\n3.End")
        n = int(input("Enter your choice: "))
        if n == 1:
            encryptText()
        elif n == 2:
            decryptText()
        else:
            break
        

    
    
