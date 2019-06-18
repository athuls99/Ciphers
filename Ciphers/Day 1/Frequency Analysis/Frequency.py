from collections import Counter

def subString(s, n): 
    k=[] 
    for i in range(n): 
        for len in range(i+1,n+1): 
            k.append(s[i: len])
    return k

def most_frequent(List,i): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0]

def FreqAnalyzer(word):
    nword=word.replace(" ","")
    s=subString(nword,len(nword))
    #print(s)
    temp1=[]
    for i in s:
        if (len(i)==2):
            temp1.append(i)
    #print(temp1)
    for i in range(2):
        c=most_frequent(temp1,i)
        #print(c)
        nword=nword.replace(c,Common_Bigrams[i])
    return nword
    
    


letter_freq = 'etaoinsrhdlucmfywgpbvkxqjz'


def Freq_Dist(text):
	frequency_dictionary = {}
	for letter in text:
		if not letter.isalpha():
			continue
		key = letter.lower()
		if key in frequency_dictionary:
			frequency_dictionary[key] += 1
		else:
			frequency_dictionary[key] = 1
	return frequency_dictionary


def Order_Freq_Dist(freq_dict):
	return sorted(freq_dict, key=freq_dict.get, reverse=True)


def Substitute(text, freq_dict):
	new_sentence = ""
	for letter in text:
		if not letter.isalpha():
			new_sentence += letter
		else:
			order = freq_dict.index(letter.lower())
			new_letter = letter_freq[order]
			if letter.isupper():
				new_sentence += new_letter.upper()
			else:
				new_sentence += new_letter
	return new_sentence

expectedvalues = {'a':0.082,'b':0.015,'c':0.028,'d':0.042,'e':0.127,'f':0.022,'g':0.020,
                 'h':0.061,'i':0.07,'j':0.002,'k':0.008,'l':0.040,'m':0.024,'n':0.068,
                 'o':0.075,'p':0.02,'q':0.001,'r':0.06,'s':0.063,'t':0.090,'u':0.028,
                 'v':0.01,'w':0.024,'x':0.002,'y':0.02,'z':0.001}
Common_Bigrams = [    'TH',        'EN',        'NG',
                      'HE',        'AT',        'AL',
                      'IN',        'ED',        'IT',
                      'ER',        'ND',        'AS',
                      'AN',        'TO',        'IS',
                      'RE',        'OR',        'HA',
                      'ES',        'EA',        'ET',
                      'ON',        'TI',        'SE',
                      'ST',        'AR',        'OU',
                      'NT',        'TE',        'OF']

text=input("Enter string to be decrypted : ")
freq_dict = Freq_Dist(text)
freq_dict = Order_Freq_Dist(freq_dict)
decoded_text=Substitute(text, freq_dict)
print(decoded_text)
decoded_text=FreqAnalyzer(decoded_text)
print(decoded_text)