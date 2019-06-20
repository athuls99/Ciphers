def preProcessText(text,flag,colSize):
    text=text.upper()
    text=text.replace(" ","")
    if(not flag):
        remain = len(text)%colSize
        remain = colSize-remain
        rmStr = ""
        if(remain != 3):
            for i in range(remain):
                rmStr += "Z"
        text = text + rmStr
    return text
def createMatrix(colSize,textLen):
    rowSize = int(textLen / colSize)
    textMatrix = []
    for i in range(rowSize):
        temp = []
        for j in range(colSize):
            temp.append(-1)
        textMatrix.append(temp)
    #print(textMatrix,rowSize,colSize,text)
    return textMatrix

def encrypt(text,colSize):
    textMatrix= createMatrix(colSize,len(text))
    rowSize = int(len(text) / colSize)
    k=0
    for i in range(rowSize):
        for j in range(colSize):
            textMatrix[i][j] = [text[k],-1]
            k+=1
    print(textMatrix)
    moveLeft=0
    moveRight=1
    moveUp=0
    moveDown=0
    xpos = 0
    ypos = 0
    count = 1
    val = rowSize * colSize
    n=rowSize
    m=colSize
    count = 1
    encryptedString =""
    while(count <= val-1):
        if(moveDown):
            if(xpos != n-1 and (textMatrix[xpos + 1][ypos][1] == -1)):
                encryptedString += textMatrix[xpos][ypos][0]
                textMatrix[xpos][ypos][1] = count
                count += 1
                xpos += 1
            else:
                moveLeft = 1
                moveDown=0
        elif(moveUp):
            if(xpos != 0 and (textMatrix[xpos - 1][ypos][1] == -1)):
                encryptedString += textMatrix[xpos][ypos][0]
                textMatrix[xpos][ypos][1] = count
                count += 1
                xpos -= 1
            else:
                moveRight = 1
                moveUp = 0
        elif(moveRight):
            if(ypos != m-1 and (textMatrix[xpos][ypos + 1][1] == -1) ):
                encryptedString += textMatrix[xpos][ypos][0]
                textMatrix[xpos][ypos][1] = count
                count += 1
                ypos += 1
            else:
                moveDown = 1
                moveRight = 0
        elif(moveLeft):
            if(ypos != 0 and (textMatrix[xpos][ypos - 1][1] == -1)):
                encryptedString += textMatrix[xpos][ypos][0]
                textMatrix[xpos][ypos][1] = count
                count += 1
                ypos -= 1
            else:
                moveUp = 1
                moveLeft = 0
    encryptedString += textMatrix[xpos][ypos][0]
    #print(textMatrix)
    return encryptedString


def decrypt(text,colSize):
    textMatrix= createMatrix(colSize,len(text))
    rowSize = int(len(text) / colSize)
    moveLeft=0
    moveRight=1
    moveUp=0
    moveDown=0
    xpos = 0
    ypos = 0
    count = 1
    val = rowSize * colSize
    n=rowSize
    m=colSize
    count = 1
    while(count <= val-1):
        if(moveDown):
            if(xpos != n-1 and (textMatrix[xpos + 1][ypos] == -1)):
                textMatrix[xpos][ypos] = text[count-1]
                count += 1
                xpos += 1
            else:
                moveLeft = 1
                moveDown=0
        elif(moveUp):
            if(xpos != 0 and (textMatrix[xpos - 1][ypos] == -1)):
                textMatrix[xpos][ypos] = text[count-1]
                count += 1
                xpos -= 1
            else:
                moveRight = 1
                moveUp = 0
        elif(moveRight):
            if(ypos != m-1 and (textMatrix[xpos][ypos + 1] == -1) ):
                textMatrix[xpos][ypos] = text[count-1]
                count += 1
                ypos += 1
            else:
                moveDown = 1
                moveRight = 0
        elif(moveLeft):
            if(ypos != 0 and (textMatrix[xpos][ypos - 1] == -1)):
                textMatrix[xpos][ypos] = text[count-1]
                count += 1
                ypos -= 1
            else:
                moveUp = 1
                moveLeft = 0
    textMatrix[xpos][ypos] = text[count-1]
    decryptedString = ""
    for i in range(rowSize):
        for j in range(colSize):
            decryptedString += textMatrix[i][j]
    
    return decryptedString

if __name__ == "__main__":  
    n=int(input("ENTER 0 TO ENCRYPT OR 1 TO DECRYPT\n"))
    colSize = int(input("ENTER COLUMN SIZE (Key)"))
    # Enter route 1.Spiral inward CW 2.Spiral inward ACW
    if(not n):
        text=input("ENTER THE PLAIN TEXT\n")
        text = preProcessText(text,n,colSize)
        encryptedString = encrypt(text,colSize)
        print("THE ENCRYPTED STRING IS :")
        print(encryptedString)
    else:
        text= input("ENTER THE ENCRYPTED TEXT\n")
        text = preProcessText(text,n,colSize)
        decryptedString = decrypt(text,colSize)
        print(decryptedString)
