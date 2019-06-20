alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']

def get_key(key_input, alphabet):
    key = []
    for char in key_input:
        if char in alphabet and char not in key: # add the character to the matrix if it's valid and not already in the matrix
            key.append(char)
    for char in alphabet:
        if char not in key: # add the rest of the alphahet not appearing in the key to the matrix
            key.append(char)
    return key


def gen_matrix(key):
    matrix = []
    counter = 0
    for xcounter in range(5):
        x = []
        for ycounter in range(5):
            x.append(key[counter])
            counter += 1
        matrix.append(x)
    return matrix


def print_matrix(matrix):
    for counter in range(5):
        print (matrix[counter][0], matrix[counter][1], matrix[counter][2], matrix[counter][3], matrix[counter][4])

def decrypt(message, key1, key2):
    char = 'J'
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if (char not in key1) and ( char not in key2) and (char not in message): 
        #print("\nOmitting Letter: %s " % char)
        alphabet.remove(char)
    else:
        alphabet.remove('I')
    #print("Alphabet Matrix:")
    matrix2 = gen_matrix(alphabet)
    #print_matrix(matrix2)
    #print("Keyed Matrix1:")
    alpha_key1 = get_key(key1, alphabet)
    matrix_key1 = gen_matrix(alpha_key1)
    #print_matrix(matrix_key1)
    #print("Keyed Matrix2:")
    alpha_key2 = get_key(key2, alphabet)
    matrix_key2 = gen_matrix(alpha_key2)
    #print_matrix(matrix_key2)

    plaintext = []
    i = 0
    for d in message:
        if (i % 2 == 0) :
            coords1 = get_coords(d, matrix_key1)
            action = 0
        else:
            coords2 = get_coords(d, matrix_key2)
            action = 1
        i += 1
            
        if ( action ):
            x, y = ((coords1[0][0], coords2[0][1]))
            plaintext.append(matrix2[x][y])
            x, y = ((coords2[0][0], coords1[0][1]))
            plaintext.append(matrix2[x][y])
            
    return ''.join(plaintext).lower()

def encrypt(message, key1, key2):
    message=message.replace(" ","")
    char = 'J'
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if (char not in key1) and ( char not in key2) and (char not in message): 
        print("\nOmitting Letter: %s " % char)
        alphabet.remove(char)
    else:
        alphabet.remove('I')

    print("Alphabet Matrix:")
    matrix2 = gen_matrix(alphabet)
    print_matrix(matrix2)
    print("Keyed Matrix1:")
    alpha_key1 = get_key(key1, alphabet)
    matrix_key1 = gen_matrix(alpha_key1)
    print_matrix(matrix_key1)
    print("Keyed Matrix2:")
    alpha_key2 = get_key(key2, alphabet)
    matrix_key2 = gen_matrix(alpha_key2)
    print_matrix(matrix_key2)

    plaintext = []
    i = 0
    if not len(message)%2 == 0:
        message += 'X' 
    for d in message:
        if (i % 2 == 0) :
            coords1 = get_coords(d, matrix2)
            action = 0
        else:
            coords2 = get_coords(d, matrix2)
            action = 1
        i += 1
            
        if ( action ):
            x, y = ((coords1[0][0], coords2[0][1]))
            plaintext.append(matrix_key1[x][y])
            x, y = ((coords2[0][0], coords1[0][1]))
            plaintext.append(matrix_key2[x][y])
            
    return ''.join(plaintext)


def get_coords(digraph, key_matrix):
    coords = []
    for char in digraph:
        for x in range(5):
            for y in range(5):
                if key_matrix[x][y] == char:
                    coords.append((x,y))
    return coords
                    

def main():
    print ("Enter Key1:")
    key1 = input().upper()
    print ("Enter Key2:")
    key2 = input().upper()
    print("Enter 0 to encrypt or 1 to decrypt")
    m=int(input())
    if(m==0):
            print("Enter the message you would like to encrypt. \nThe only valid characters are the letters A-Z.")
            message = input()
            print("The message you entered is:", message)
            plaintext = encrypt(message.upper(), key1, key2)
            print ("Your encrypted message is  : " , plaintext)
            print("/n")
    if(m==1):
            print("Enter the message you would like to decrypt. \nThe only valid characters are the letters A-Z.")
            message = input()
            print("The message you entered is:", message)
            plaintext = decrypt(message.upper(), key1, key2)
            print ("Your decrypted message is  : " , plaintext)
            print("/n")


if __name__ == "__main__":
    main()
