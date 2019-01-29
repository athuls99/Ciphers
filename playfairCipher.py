print("Enter the message");
message = input();
message = message.upper();
message=message.replace(" ","")
messagePair= [];
length = len(message);
i=0;
print("Enter Keyword(the word should not have a repeated charecter)");
keyword = input();
keyword = keyword.upper();
while(i<length-1):
    if(message[i]!= message[i+1]):
        messagePair.append(message[i]+message[i+1])
        i=i+2;
    else:
        messagePair.append(message[i]+ "X")
        i=i+1;
if(i==length-1):
    messagePair.append(message[i]+ "X")
alpha = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alpha.sort();
encrypt = [[],[],[],[],[]]
keyLength = len(keyword)
f=0
count =0;
for i in range(0,5):
    for j in range(0,5):
        if((5*i)+j<keyLength):
            print(i,j)
            encrypt[i].append(keyword[(5*i)+j])
            alpha.remove(keyword[(5*i)+j])
        else:
            encrypt[i].append(alpha[count])
            count+=1;
    if(f):
        break;

print(encrypt,alpha,messagePair);
index = [];

for i in messagePair:
    for j in encrypt:
        if(i[0] in j):
            temp1y = j.index(i[0])
            temp1x = encrypt.index(j)
        if(i[1] in j):
            temp2y = j.index(i[1])
            temp2x = encrypt.index(j)
    index.append((temp1x,temp1y,temp2x,temp2y))
print(index)

final = [];
for val in index:
    if(val[0] == val[2]):
        nextx1 = val[0];
        nextx2 = val[2];
        nexty1 = (val[1]+1)%5
        nexty2 = (val[3]+1)%5
        final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])
    elif(val[1] == val[3]):
        nextx1 = (val[0]+1)%5
        nextx2 = (val[2]+1)%5
        nexty1 = val[1];
        nexty2 = val[3];
        final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])
    else:    
        nextx1 = val[0]
        nextx2 = val[2]
        nexty1=val[3]
        nexty2=val[1]
        final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])
print(final)
