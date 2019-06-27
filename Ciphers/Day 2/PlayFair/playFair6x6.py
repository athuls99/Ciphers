from wordsegment import load,segment
import re
load()
#pairing the individual charecters together and storing pairs in messagePair array
def Pair(message,messagePair):
        length = len(message)
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
def fill(encrypt,alpha,keyword):
        keyLength = len(keyword)
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
def getIndex(messagePair,encrypt,ind):
    for i in messagePair:
        for j in encrypt:
            if(i[0] in j):
                temp1y = j.index(i[0])
                temp1x = encrypt.index(j)
            if(i[1] in j):
                temp2y = j.index(i[1])
                temp2x = encrypt.index(j)
        ind.append((temp1x,temp1y,temp2x,temp2y))
    return ind
def encryptMessage(encrypt,index):
        final = []
        for val in index:
            #if the two charecters lie on the same row, keep the row same and increment the column by one
            # with wrap around
            if(val[0] == val[2]):
                nextx1 = val[0]
                nextx2 = val[2]
                nexty1 = (val[1]+1)%6
                nexty2 = (val[3]+1)%6
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

            #if the two charecters lie on the same column, keep the column same and increment the row by one
            # with wrap around    
            elif(val[1] == val[3]):
                nextx1 = (val[0]+1)%6
                nextx2 = (val[2]+1)%6
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
def decryptPair(message,messagePair):
        length = len(message)
        i=0
        while(i<length-1):
                messagePair.append(message[i]+message[i+1])
                i=i+2
        return messagePair

def decryptMessage(encrypt,index):
        final = []
        for val in index:
            #if the two charecters lie on the same row, keep the row same and increment the column by one
            # with wrap around
            if(val[0] == val[2]):
                nextx1 = val[0]
                nextx2 = val[2]
                nexty1 = (val[1]-1)
                nexty2 = (val[3]-1)
                if(nexty1 == -1):
                        nexty1 = 5
                if(nexty2 == -1):
                        nexty2 = 5        
                final.append(encrypt[nextx1][nexty1] + encrypt[nextx2][nexty2])

            #if the two charecters lie on the same column, keep the column same and increment the row by one
            # with wrap around    
            elif(val[1] == val[3]):
                nextx1 = (val[0]-1) 
                nextx2 = (val[2]-1)
                nexty1 = val[1]
                nexty2 = val[3]
                if(nextx1 == -1):
                        nextx1 = 5
                if(nextx2 == -1):
                        nextx2 = 5
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
        finalval = []
        f=0
        for i in range(0,length):
                f=0
                if(String[i] == "Z"):
                        if((i-1)>=0 and i+1 < length):
                                if(String[i-1] == String[i+1]):
                                        f=1
                if(not f):
                        if(length%2 == 0 and i == length-1 and String[i] == "Z"):
                                pass
                        else:
                                finalval.append(String[i])
        return finalval    

def preprocess(opt,text,key):
        text = re.sub(r'[^A-Za-z0-9]',"",text)
    
        key = key.replace(" ","")
        messagePair= []
        if(opt == 0):
                messagePair = Pair(text,messagePair)
        else:
                messagePair = decryptPair(text,messagePair)
        encrypt = [['A','B','C','D','E','F'],['G','H','I','J','K','L'],['M','5','6','7','8','9'],['0','1','2','3','4','N'],
        ['O','P','Q','R','S','T'],['U','V','W','X','Y','Z']]
        ind = []
        ind = getIndex(messagePair,encrypt,ind)
        return (encrypt,ind)

if __name__ == "__main__":    
        print("Enter the message")
        message = """EFDODT KC3FQK QLQYLQ KPU0KY GB8APL FOL2QU SDFGKQ BKQUAT URGJPK JIBUFC DYF4PL KYJH2L CLDB2F ASLZKB TOOD0L FKBCPS FOPSUE RZOPAJ DSRYPK UAJFGB YBCFYD 0THBGQ YOUASQ SDOY5O QLT0PL FOZRKB SDAQYB SXTAUA SQGF4T SFO7L2 FOFEPL FO0UTO Z0THFB OETZL2 I6EFTZ C6JZGJ AFDOGB Z0OZQK TZKBEB EYF0CX DYK8OE KBBEAV OFJZGT U6FSSA VRGFL2 FODOFD F4O9DY FSL2MU LZKBSP UEKTQA KCSZBD TGZJFB MADSFS XO2L0L DTU0DT F0DFUA Z9L2FE OP8APL CYPSGS A9EBMA DSDXAS TZKBCL WJ0LTA G6GMKY VOT0HG EOYRTH FOKYIJ TQSPDF RYRYQK 6GGFQJ 4TQHQJ RZOPPL FOA8TH SUFEEV UASPZ2 7OOFHF POKQC6 PLG6U7 L2F4OT VOVRPS ZLSP5G KQQU0L PUDS09 F4QFGT YKOPAQ 7U8AQD GCKTWA WDKYYR PLFEKY DQHQQL T0TAPL BSSPDF RYQK0F O8WAGB QKQLY8 0TZ2UA OTJCFB FIPTFD JQFICK 1ZTGYB TOKBYB SXAQ5O UA3FRE KQAQYB SDCJTZ KBAPDO CJ0LGP YOAKHW F4PLFA SD2FIJ TZDSKY QL0TXO EFQKL0 OE3FPL CKSDVR DSQLYK L2PLBS GPOPJO BOIJDB SOQKQZ UAJFCF OPUR0A BIOPEO YRA0FS IJOEAQ L2I6EF 2FCKAF DOPLFO FGSDBE ZSKBAQ QHFEDJ KYJH4T DOCKTL PSCKL0 GB3FTP 0F0USD PQQL6G TO6I0T SFJIBU A8BEFB 0UTOSD 0GSJBC KF0GPL A8FO6I FGCJQE PUDSWK QZJGZJ FGZJQU YOOPEF YBGTOB 4FCIHQ KBQXIJ BIARKY 0TOSCS WGSDPL KYFDSD RFKQOS HCZOGQ 0TAF2F SXQOGQ 4LKETS FOKBSO KBAQ1Z DSYKT0 A8EUOV FHKQLP KBYD2F SXQOGQ 4LKEDT DYFKE8 DYBSL2 KOFDSD OPT9ZS KB8KZS RAFDHQ KBQJ0L 6IFGZJ PLKQ4F U6FSGP FRKBSD 0GSJBC KZYKAW SDDOQL CLDFI6 V5DS8A RYOEKA OESDCL STSF2F RAFEEO 0Z5ADS OYQK0L TP8AGM SDYDA7 FDGB2L O8PLKY DYF4AQ EFA7KY YRGMKY DOFSKB 4F2FHQ KBSDEC EKVRT0 F4QLFO L2LOKB 9OPOKB YKYBTZ 5VQUDS 0UAXGT PLBSSP AXFQTA QZPQQJ 8A0Z5A DSOYQK 0LPLDS A8DOGE FHDSKY ZGOTTA ZDDS0G OP4F0G XEFDHQ KBSOKB 8ARYOE KAPEUE 0TPLDS DYQP4F TZGCQL T0GPYC YBQXLQ GPZOL4 QUKFAJ ASLZKB QZPQQJ 8ATOKB YDVRT0 F4QLYK ZRSD8A KZCJDZ CLAW9Z ZRRAFS DS6G4F HJYBTZ KBCJDZ CLAW9Z USDZAB FQPSKQ L2LOKB GFOJCK TZAKDS T0A8EU OVFHKQ LPKBQS RAWAOT FDXOCK TZKBL4 QUKFAJ FSGBRZ PLBSQJ 8ATOKB 8OFKYB OESDAQ 2FFBKF FRGPAM IJO9YO PFKYCG FRGBOL HWF4PL DSKYUA QDKYPL BSSPFH A8TAZD BDOPQJ OEQLT0 LQYK9L 0GZYWK FKFRPO KBQPYC STTAPL FB0FKZ QLDF0L L2CYDS CKSFYB SOPAFC WG9ZEV UCUSCL JZGZTO ODQLT0 TAPLKY FDXOLQ USLZIJ O8FSGP EXUA0G ZXKQLP PTDYCK EZUADB TLL2FR KBQZPQ QJ8AAB FQPSTP DN25W7 6NN27M 273V2V BKBUF4 QUYOFE PLKQTH EUABJQ I6V5DS QZ6IFB 3F6CEO 6G3FFE OPOYJU KATOZR GBQZKY GPZGBR DSGBQT BIF0KA OPF0PO KBO7FS GPECZO FGZJPL KQSDL9 FDQLT0 T0Z3A0 DS6IFG ABFQPS PEQJ0L TOU0L2 EBAZSO KBT3FO XOFGUB QJFOGQ 0TATXO AWXDSD TZI6V5 DSSBPJ BOYEUA 6GHIOS KYQP3F YOL2HJ SZUAST EOBYDS DP"""
        message = message.upper()
        message=message.replace(" ","")
        messagePair= []
        length = len(message)
           
        # print("Enter Keyword(the word should not have a repeated charecter)")
        # keyword = input()
        # keyword = keyword.upper()
        print("Enter 0 encrypt and 1 to decrypt")
        check = int(input())
        if(check == 0):
                messagePair = Pair(message,messagePair)
        else:
                messagePair = decryptPair(message,messagePair)
        # J is removed is from the alpha array to keep to length 25 = 5X5  
        alpha = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        alpha.sort()
        
        #5X5 array
        encrypt = [['A','B','C','D','E','F'],['G','H','I','J','K','L'],['M','5','6','7','8','9'],['0','1','2','3','4','N'],
        ['O','P','Q','R','S','T'],['U','V','W','X','Y','Z']]
        #print(encrypt,alpha,messagePair)
        index = []
        index = getIndex(messagePair,encrypt,index)
        print(index,messagePair)
        final = decryptMessage(encrypt,index)
        if(check == 0):
                final = encryptMessage(encrypt,index)
                print("".join(final))
        else:
                final = decryptMessage(encrypt,index)
                print(final)
                final = "".join(final)
                final = segment(final)
                print(" ".join(final))
