import math
def matrix(key):
    matrix=[]
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for e in alphabet:
        if e not in matrix:
            matrix.append(e)    
    

    matrix_group=[]
    for e in range(5):
        matrix_group.append('')

    
    matrix_group[0]=matrix[0:5]
    matrix_group[1]=matrix[5:10]
    matrix_group[2]=matrix[10:15]
    matrix_group[3]=matrix[15:20]
    matrix_group[4]=matrix[20:25]
    return matrix_group

def encrypt(table, message):
    #string = table
    cipher = ''
    """for unused in range(len(message)):
        if " " in message:
            message.remove(" ")"""

    for ch in message.upper():
        for row in range(len(table)):
            if ch in table[row]:
                x = str((table[row].index(ch) + 1))
                y = str(row + 1)
                cipher += x + y
    return cipher

def decrypt(table, numbers):
    text = ''
    for index in range(0, len(numbers), 2):
        y = int(numbers[index]) - 1
        x = int(numbers[index + 1]) - 1
        text += table[x][y]
    return text


if __name__ == "__main__":
    order=int(input("Choose :\n1,Encrypting \n2,Decrypting\n"))
    if order==1:
        key=input("Please input key :")
        message=input("Please input the message (only from A-Z): ")
        print ("Matrix : ")
        print (matrix(key))
        matrix=matrix(key)
        print ("Cipher: ") 
        print (encrypt(matrix,message))
    elif order==2:
        key=input("Please input key  : ")
        matrix=matrix(key)
        cipher=input("Please input the cipher text: (only from A-Z)")
        print ("Plaintext:")
        print (decrypt(matrix,cipher))
    else:
        print ("Error")
