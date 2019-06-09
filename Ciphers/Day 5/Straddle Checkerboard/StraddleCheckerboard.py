def preProcessText(text):
    text=text.upper()
    text=text.replace(" ","")
    return text
def constructBoard(key,c1,c2):
    checkerBoard = []
    for i in range(3):
        temp=[]
        for j in range(10):
            temp.append(-1)
        checkerBoard.append(temp)
    checkerBoard[0][c1] = ""
    checkerBoard[0][c2] = ""
    checkerBoard[1][1] = " "
    checkerBoard[2][9] = "#"
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    frequentOrder = "ETAOINSR"
    #pprint(key)
    for i in key:
        if(i not in frequentOrder):
            frequentOrder += i
    flen = len(frequentOrder)
    val = 0
    count =0
    for i in range(3):
        for j in range(10):
            if(checkerBoard[i][j] == -1):
                if( val < flen):
                    checkerBoard[i][j] = frequentOrder[val]
                    alpha.remove(frequentOrder[val])
                    val += 1
                else:
                    checkerBoard[i][j] = alpha[count]
                    count += 1
    return(checkerBoard)
def getVal(elem,checkerBoard,c1,c2):
    for i in range(3):
        for j in range(10):
            if(checkerBoard[i][j] == elem):
                if(i==0):
                    return (str(j))
                elif(i==1):
                    return (str(c1)+str(j))
                else:
                    return (str(c2)+str(j))
def encrypt(text,checkerBoard,c1,c2):
    encryptedString = ""
    for i in text:
        encryptedString += getVal(i,checkerBoard,c1,c2)
    print(encryptedString)
def decrypt(text,checkerBoard,c1,c2):
    decryptedString =""
    i=0
    while(i < len(text)):
        if((int(text[i]) == c1) or (int(text[i]) == c2)):
            if(int(text[i]) == c1):
                decryptedString += checkerBoard[1][int(text[i+1])]
            elif(int(text[i]) == c2):
                decryptedString += checkerBoard[2][int(text[i+1])]
            i+=2
        else:
            decryptedString += checkerBoard[0][int(text[i])]
            i+=1
    print(decryptedString)
key = input("Enter the keyword\n")
key = preProcessText(key)
ckeys = list(map(int,input("Enter the columns-key for the checker board\n").split()))
c1 = ckeys[0]
c2 = ckeys[1]
checkerBoard = constructBoard(key,c1,c2)
flag = int(input("Enter 0 to encrypt and 1 to decrypt\n"))
if(not flag):
    text = input("Enter plain text\n")
    text=text.upper()
    encrypt(text,checkerBoard,c1,c2)
else:
    text = input("Enter encrypted text\n")
    #text = preProcessText(text)
    decrypt(text,checkerBoard,c1,c2)
