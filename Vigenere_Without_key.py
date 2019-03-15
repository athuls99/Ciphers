from collections import Counter

#Generates all 26 caesr cipher combinations alphabetically.
#might contain bugs
#please check

def gen_26_combn(enc_string):
    temp=enc_string.upper()
    k=0
    combn=[]
    for i in range(0,26):
        string=""
        for j in temp:
            if (((ord(j)-i)%26)<0):
                string+=chr(91-((ord(j)-i)%26))
            else:
                string+=chr(65+((ord(j)-i)%26))
        combn.append(string)
    return combn

#Decryptor function once you guess the right key 

def Decryptor(Encrypted_string,key):
    l=len(key)
    j=0
    dec_string=""
    dchar=0
    for i in Encrypted_string:
        if (i.isupper() and key[j].isupper()):
            dchar=65+(ord(i)-ord(key[j])+26)%26
        elif (i.islower() and key[j].islower()):
            dchar=97+((ord(i)-ord(key[j])+26)%26)
        dec_string+=chr(dchar)
        j=(j+1)%l
    return dec_string

#Chi square analysis function

def chi_sq(enc_s):
    #exp_count = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
    expectedvalues = {'a':0.08167,'b':0.01492,'c':0.02782,'d':0.04253,'e':0.12702,'f':0.02228,'g':0.02015,
                 'h':0.06094,'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,'m':0.02406,'n':0.06749,
                 'o':0.07507,'p':0.01929,'q':0.00095,'r':0.05987,'s':0.06327,'t':0.09056,'u':0.02758,
                 'v':0.00978,'w':0.02360,'x':0.00150,'y':0.01974,'z':0.00074}
    chi_sq=[]
    temp=0
    p=dict(Counter(enc_s))
    print(p)
    #enc_string=enc_s.upper()
    tcount=len(enc_s)
    for i in enc_s:
        chi_sq.append(((p[i]-(expectedvalues[i.lower()]*tcount))**2)/(expectedvalues[i.lower()]*tcount)**2)
    return sum(chi_sq)

#From here's where I went wrong
#this function basically takes the appropriate key lengths
#breaks the string in the similar manner
#generates all 26 possible caese cipher combinations
#Finds a single alphabet of the key

#This one function has not been implemented properly.
#If you can help me fix this function then it will work.

def Chk_key(Enc_string,i):
    l=len(Enc_String)
    chiv=[]
    r="".join(Enc_String[p] for p in range(0,l,i))
    #chiv.append(chi_sq(r))
    #print
    pop=gen_26_combn(r)
    print(pop)
    k=0
    n=0
    for i in pop:
        k=chi_sq(i)
        if (k<=80):
            chiv.append((k,n))
            print("Possible Key:",r)
            print(Decryptor(Enc_string,r))
        n+=1
        
            
#Finding Index of Coincdence
#finding index of coincidence for strings of all possible keys
#breaking the strings into multiple strings of key size
#Finding index of coincidence of each one of them
#this will give us a list of appropriate/possible key lengths.
        
def IC(string1,k):
    l=len(string1)
    #print(l)
    s=[]
    r=""
    p=0
    j=0
    kl=0
    iocs=[]
    for i in range(k):
        r="".join(string1[p] for p in range(j,l,k))
        s.append(r)
        if (j<k):
            j+=1
        #print("R=",r)
        
        p+=1
    print(s)
    #print("R=",r)
    for i in s:
        iocs.append(get_ic(i))
    return sum(iocs)/k
        
        

#Function to calculate index of coincedence of a string
def get_ic(s):
    n=len(s)
    ic=0
    if n-1:
        ic=(1/(float(n)*(n-1)))*(sum([s.count(a)*(s.count(a)-1) for a in set(s)]))
    return ic

#Removing all spaces from the string and passing the string to index of coincience function for different keys.
#The Index of Coincidence (I.C.) is a statistical technique that gives an indication of how English-like a piece of text is.
#One of the useful properties of the technique is that the result of the I.C. does not change if you apply a substitution cipher to the text.
#This is because the I.C. is based on letter frequencies, and simple substitution ciphers do not modify the individual letter frequencies.
#If text is similar to english it will have an I.C. of around 0.06, if the characters are uniformly distributed the I.C. is closer to 0.03-0.04.
#what we are basically trying to do is find the period of repitition which will give us the key length.
def IOC(Enc_string):
    i=1
    mod_string="".join(Enc_string.split())
    print(mod_string)
    l=len(mod_string)
    pk=[]                                        #List of possible keys
    while (i<=(l/2)):                            #Assuming max key length=Half times size of word
        if (IC(mod_string,i)>=0.09):
            pk.append(i)
        i+=1
    return pk
        
def decryptor(Enc_string):
    Possible_Key_Lengths=IOC(Enc_string)        #IOC -Index of Coincidence function
    print(Possible_Key_Lengths)
    for i in Possible_Key_Lengths:
        Chk_key(Enc_string,i)

Enc_String=input("Enter the Encrypted text:")
decryptor(Enc_String)
