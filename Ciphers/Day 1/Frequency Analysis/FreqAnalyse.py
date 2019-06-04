import * from collections

def FreqAnalyzer(word):
    k=int(len(word)/2)
    nword=word
    s=Counter(word).most_common()
    for i in range(len(word)):
        nword=nword.replace

expectedvalues = {'a':0.082,'b':0.015,'c':0.028,'d':0.042,'e':0.127,'f':0.022,'g':0.020,
                 'h':0.061,'i':0.07,'j':0.002,'k':0.008,'l':0.040,'m':0.024,'n':0.068,
                 'o':0.075,'p':0.02,'q':0.001,'r':0.06,'s':0.063,'t':0.090,'u':0.028,
                 'v':0.01,'w':0.024,'x':0.002,'y':0.02,'z':0.001}
word=input("Enter string to be decrypted : ")


