def encrypt(message,key,alpha):
    string=""
    for char in message:
        if char in alpha:
            string+=char
    index_values=[alpha.index(char) for char in string]
    return "".join([key[ind] for ind in index_values]).upper()

def decrypt(message,key,alpha):
    string=""
    for char in message:
        if char in alpha:
            string+=char
    index_values=[key.index(char) for char in string]
    return "".join([alpha[ind] for ind in index_values]).lower()


def preProcess(user_key):
    alpha="abcdefghijklmnopqrstuvwxyz"
    key=""
    for char in user_key:
        if char in alpha:
            if char not in key:
                key+=char
    for char in alpha:
        if char not in key:
            key+=char
    return (key,alpha)

if __name__ == "__main__":
    alpha="abcdefghijklmnopqrstuvwxyz"
    print ("Enter Key:")
    user_key = input().lower()
    key=""
    for char in user_key:
        if char in alpha:
            if char not in key:
                key+=char
    for char in alpha:
        if char not in key:
            key+=char
        
    print("Enter 0 to encrypt or 1 to decrypt")
    m=int(input())
    if(m==0):
        message=input("Enter message:").lower()
        print("The encrypted text is :")
        print(encrypt(message,key,alpha))
    if(m==1):
        message=input("Enter cipher text:").lower()
        print("The decrypted text is :")
        print(decrypt(message,key,alpha))