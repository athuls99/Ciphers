#Program to encrypt and decrypt text based on Hill Cypher

#Dependencies
from functions import encryptor,decryptor

#main
if __name__ == "__main__":
    while True:
        print("1.Encrypt\n2.Decrypt with key\n")
        opt = int(input("Enter the option: "))
        if opt == 1:
            encryptor()
        elif opt == 2:
            decryptor()