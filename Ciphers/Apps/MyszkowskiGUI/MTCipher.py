from functions import encryptor,decryptor

if __name__ == "__main__":
    while True:
        print("1. Encrypt\n2. Decrypt\n 3. End\n")
        option = int(input("Enter the option: "))
        if option == 1:
            encryptor()
        elif option == 2:
            decryptor()
        else:
            break
        
    