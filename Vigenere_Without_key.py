#Finding Index of Coincdence

def IC(string,k):
    l=len(string)
    s=[]
    r=""
    p=0
    j=0
    for i in range(k):
        while (j<l):
            r+=string(j)
            j+=k
            s[p].append(



                
def IOC(Enc_string):
    mod_string="".join(Enc_string.split())
    l=len(mod_string)
    pk=[]                                        #List of possible keys
    while (i<=(l/2)):                            #Assuming max key length=Half times size of word
        if (IC(mod_string,i)>0.06):
            pk.append(i)
        i+=1
        
        
def decryptor(Enc_string):
    Possible_Key_Lengths=IOC(Enc_string)        #IOC -Index of Coincidence function
    


Enc_String=input("Enter the Encrypted text:")
decrypt(Enc_String)
