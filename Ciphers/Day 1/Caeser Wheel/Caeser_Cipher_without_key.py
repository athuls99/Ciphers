#proper decrypt file


#dependencies
from collections import Counter
from time import *
from wordsegment import load, segment

#---------------------------------------------------------------------------------------

#The referred distribution
expectedvalues = {'a':0.082,'b':0.015,'c':0.028,'d':0.042,'e':0.127,'f':0.022,'g':0.020,
                 'h':0.061,'i':0.07,'j':0.002,'k':0.008,'l':0.040,'m':0.024,'n':0.068,
                 'o':0.075,'p':0.02,'q':0.001,'r':0.06,'s':0.063,'t':0.090,'u':0.028,
                 'v':0.01,'w':0.024,'x':0.002,'y':0.02,'z':0.001}
expectedorder = sorted(expectedvalues,key = lambda x: expectedvalues[x], reverse =True)

#---------------------------------------------------------------------------------------

#functions

def preprocess(encryptedtext):
    #encryptedtext.replace(" ","")
    #encryptedtext=encryptedtext.replace("\n","")
    encryptedtext=''.join([e for e in encryptedtext if e.isalpha()])
    return encryptedtext
    

def decrypt(text,key):
    dtext = ''
    for j in range(len(text)):
        chrtemp = encryptedtext[j]
        if chrtemp.isalpha():
            if chrtemp.islower():
                temp = ord(chrtemp) - 97 - (key%26)
                if temp < 0:
                    temp = 26 + temp
                chrtemp = chr(temp+97)
            else:
                temp = ord(chrtemp) - 65 - (key%26)
                if temp < 0:
                    temp = 26 + temp
                chrtemp = chr(temp+65)
        dtext = dtext + chrtemp
    return dtext

def calchi(text):
    done = []
    chivalue = 0
    othervalues = len(text)
    counts = Counter(text)
    for j in range(len(text)):
        if j not in done:
            #count the occurences of the given character in the text
            obscount = counts[text[j]]
            #get count of the character according to the distribution
            expcount = expectedvalues[text[j]]*len(text)
            othervalues -= expcount
            chisq = obscount - expcount
            chisq = (chisq**2)/expcount
            chivalue+=chisq
    return chivalue + othervalues

#---------------------------------------------------------------------------------------

#the program
load()
encryptedtext = input("Enter the encrypted string: ")
encryptedtext=preprocess(encryptedtext)
stime = time()
#encryptedtext = list(encryptedtext)
counts = Counter(encryptedtext.lower())
key = 0

#most frequent character in the string
mfchr = counts.most_common()[0][0] #using mostcommon function of Counter object
print(mfchr)
#iterating through the most frequently used characters in English Language
for i in expectedorder[:26:]:
    #finding difference of the most frequent chr in given string with i
    key = ord(mfchr) - ord(i)
    if key<0:
        key = key+26
    dtext = decrypt(encryptedtext,key)
    chivalue = calchi(dtext.lower())
    if chivalue < 50:
        #using segment function for proper segmentation of words
        dtext = " ".join(segment(dtext))
        print("_______________________________________________________________________________________________________________")
        print("THE DECRYPTED STRING IS : ",dtext,"\nKEY : ",key)
        print("The total time is: ",time()-stime)
        print("_______________________________________________________________________________________________________________")
        break
    
