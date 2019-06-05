from wordsegment import load,segment;
load();
#pairing the individual charecters together and storing pairs in messagePair array
def Pair(messagePair):
        i=0
        while(i<length-1):
            if(message[i]!= message[i+1]):
                messagePair.append(message[i]+message[i+1])
                i=i+2
            else:
                #if 2 consecutive charecter are same pair one with X and continue
                messagePair.append(message[i]+ "Z")
                i=i+1
        if(i==length-1):
            #if the length of the message is odd 
            messagePair.append(message[i]+ "Z")
        return messagePair
#Fill the keyword string frst into the encrypt matrix
#Sequentially fill all unique remaining characters of the alphabet
def fill(encrypt,alpha):
    count =0
    for i in range(0,5):
        for j in range(0,5):
            if((5*i)+j<keyLength):
                #print(i,j)
                encrypt[i].append(keyword[(5*i)+j])
                alpha.remove(keyword[(5*i)+j])
            else:
                encrypt[i].append(alpha[count])
                count+=1
    return (encrypt,alpha)
#getting the x,y coordinates for each charecter in each pair in messagePair array
#and storing that as a tuple with 4 elements i.e (x1,y1,x2,y2) corresponding to each pair
def getIndex(index):
    for i in messagePair:
        for j in encrypt:
            if(i[0] in j):
                temp1y = j.index(i[0])
                temp1x = encrypt.index(j)
            if(i[1] in j):
                temp2y = j.index(i[1])
                temp2x = encrypt.index(j)
        index.append((temp1x,temp1y,temp2x,temp2y))
    return index
def encryptMessage(encrypt,index,final):
        for val in index:
            #if the two charecters lie on the same row, keep the row same and increment the column by one
            # with wrap around
            if(val[0] == val[2]):
                nextx1 = val[0]
                nextx2 = val[2]
                nexty1 = (val[1]+1)%5
                nexty2 = (val[3]+1)%5
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

            #if the two charecters lie on the same column, keep the column same and increment the row by one
            # with wrap around    
            elif(val[1] == val[3]):
                nextx1 = (val[0]+1)%5
                nextx2 = (val[2]+1)%5
                nexty1 = val[1]
                nexty2 = val[3]
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

            #if they lie on different rows and colums they form a rectangle and they lie on the diagonal
            #just change them to the values of the other diagonal pair
            else:    
                nextx1 = val[0]
                nextx2 = val[2]
                nexty1=val[3]
                nexty2=val[1]
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

        return final
def decryptPair(messagePair):
        i=0
        while(i<length-1):
                messagePair.append(message[i]+message[i+1])
                i=i+2
        return messagePair

def decryptMessage(encrypt,index,final):
        for val in index:
            #if the two charecters lie on the same row, keep the row same and increment the column by one
            # with wrap around
            if(val[0] == val[2]):
                nextx1 = val[0]
                nextx2 = val[2]
                nexty1 = (val[1]-1)
                nexty2 = (val[3]-1)
                if(nexty1 == -1):
                        nexty1 = 4
                if(nexty2 == -1):
                        nexty2 = 4        
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

            #if the two charecters lie on the same column, keep the column same and increment the row by one
            # with wrap around    
            elif(val[1] == val[3]):
                nextx1 = (val[0]-1) 
                nextx2 = (val[2]-1)
                nexty1 = val[1]
                nexty2 = val[3]
                if(nextx1 == -1):
                        nextx1 = 4
                if(nextx2 == -1):
                        nextx2 = 4
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

            #if they lie on different rows and colums they form a rectangle and they lie on the diagonal
            #just change them to the values of the other diagonal pair
            else:    
                nextx1 = val[0]
                nextx2 = val[2]
                nexty1=val[3]
                nexty2=val[1]
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

        return final
def removeX(final):
        String = "".join(final)
        length = len(String)
        finalval = [];
        f=0;
        for i in range(0,length):
                f=0;
                if(String[i] == "Z"):
                        if((i-1)>=0 and i+1 < length):
                                if(String[i-1] == String[i+1]):
                                        f=1;
                if(not f):
                        if(length%2 == 0 and i == length-1 and String[i] == "Z"):
                                pass
                        else:
                                finalval.append(String[i])
        return finalval                
print("Enter the message")
message = input()
message = message.upper()
message=message.replace(" ","")
messagePair= []
length = len(message)

print("Enter Keyword(the word should not have a repeated charecter)")
keyword = input()
keyword = keyword.upper()
print("Enter 0 encrypt and 1 to decrypt")
check = int(input())
if(check == 0):
        messagePair = Pair(messagePair)
else:
        messagePair = decryptPair(messagePair)
# J is removed is from the alpha array to keep to length 25 = 5X5  
alpha = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alpha.sort()
#5X5 array
encrypt = [[],[],[],[],[]]
keyLength = len(keyword)
f=0
Assign = fill(encrypt,alpha)
encrypt = Assign[0]
alpha = Assign[1]
#print(encrypt,alpha,messagePair)
index = []
index = getIndex(index)        
#print(index)
final = []
if(check == 0):
        final = encryptMessage(encrypt,index,final);
        print("".join(final))
else:
        final = decryptMessage(encrypt,index,final);
        final = removeX(final)
        final = "".join(final)
        final = segment(final)
        print(" ".join(final))
