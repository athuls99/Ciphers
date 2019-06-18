

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


#def frequency_analysis(file_path):
	#encoded_file = open(file_path, 'r')
	#decoded_file = open('unencrypted.txt', 'w')
	#text = encoded_file.read()
text=input("Enter the text to be decrypted : ")
freq_dict = Freq_Dist(text)
freq_dict = Order_Freq_Dist(freq_dict)
decoded_text=Substitute(text, freq_dict)
print(decoded_text)

