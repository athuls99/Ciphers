#Program to encrypt and decrypt text based on Hill Cypher

#Dependencies
import functions

#main
if __name__ == "__main__":
    while True:
        print("1.Encrypt\n2.Decrypt with key\n3.Decrypt without key\n")
        opt = int(input("Enter the option: "))
        if opt == 1:
            functions.encryptor()