import math
from wordsegment import load,segment
def matrix(key):
    matrix=[]
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for e in alphabet:
        if e not in matrix:
            matrix.append(e)    
    
    #initialize a new list.
    matrix_group=[]
    for e in range(5):
        matrix_group.append('')

    #Break it into 5*5
    matrix_group[0]=matrix[0:5]
    matrix_group[1]=matrix[5:10]
    matrix_group[2]=matrix[10:15]
    matrix_group[3]=matrix[15:20]
    matrix_group[4]=matrix[20:25]
    return matrix_group

def message_to_digraphs(message_original):
    #Change it to Array. 
    message=[]
    for e in message_original:
        message.append(e)

    #Delet space
    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")

    
    #If it is odd digit, add an "X" at the end
    if len(message)%2==1:
        message.append("X")
    #Grouping
    i=0
    new=[]
    for x in range(1,math.floor(len(message)/2)+1):
        new.append(message[i:i+2])
        i=i+2
    return new

def find_position(key_matrix,letter):
    x=y=0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j]==letter:
                x=i
                y=j
                break

    return x,y

def encrypt(message,key1,key2):
    message1=message_to_digraphs(message)
    key_matrix1=matrix(key1)
    key_matrix2=matrix(key2)
    cipher=[]
    for e in message1:
        p1,q1=find_position(key_matrix1,e[0])
        p2,q2=find_position(key_matrix2,e[1])
        if q1==q2:
          cipher.append(key_matrix1[p1][q1])
          cipher.append(key_matrix2[p2][q2])
        else:
          cipher.append(key_matrix1[p1][q2])
          cipher.append(key_matrix2[p2][q1])
    return "".join(cipher)

def cipher_to_digraphs(cipher):
    i=0
    new=[]
    for x in range(math.floor(len(cipher)/2)):
        new.append(cipher[i:i+2])
        i=i+2
    return new


def decrypt(cipher,key1,key2):    
    cipher=cipher_to_digraphs(cipher)
    key_matrix1=matrix(key1)
    key_matrix2=matrix(key2)
    plaintext=[]
    for e in cipher:
        p1,q1=find_position(key_matrix1,e[0])
        p2,q2=find_position(key_matrix2,e[1])   
        if q1==q2:
            plaintext.append(key_matrix1[p1][q1])
            plaintext.append(key_matrix2[p2][q2])
        else:
            plaintext.append(key_matrix1[p1][q2])
            plaintext.append(key_matrix2[p2][q1])
    
    output=""
    for e in plaintext:
        output+=e
    
    output = segment(output)
    if 'x' in output[-1] and len(output[-1]) == 1:
        output = output[:-1]
    return " ".join(output).lower()

#key="cipher"
#message="effecttreecorrectapple"
#cipher="FNNFHOODPZCIVGFCHOBIBSPZ"

#key="playfairexample"
#message="Hide the gold in the tree stump"
#>>BMODZBXDNABEKUDMUIXMMOUVIF

if __name__ == "__main__":
    order=int(input("Choose :\n1,Encrypting \n2,Decrypting\n"))
    if order==1:
        key1=input("Please input key 1: ")
        key2=input("Please input key 2: ")
        message=input("Please input the message (only from A-Z): ")
        #print ("Encrypting: \n"+"Message: "+message)
        #print ("Break the message into digraphs: ")
        #print (message_to_digraphs(message))
        #print ("Matrix 1: ")
        #print (matrix(key1))
        #print ("Matrix 2: ")
        #print (matrix(key2))
        print ("Cipher: ") 
        text = encrypt(message.upper(),key1,key2)
        print(text)
    elif order==2:
        key1=input("Please input key 1 : ")
        key2=input("Please input key 2 : ")
        cipher=input("Please input the cipher text: (only from A-Z)")
        #cipher="ILSYQFBWBMLIAFFQ"
        print ("\nDecrypting: \n"+"Cipher: "+cipher)
        print ("Plaintext:")
        text = decrypt(cipher,key1,key2)
        print(text)
    else:
        print ("Error")
