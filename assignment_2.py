def translate_numeral(number):
	if type(number) == str:  # check type of input
		roman_numeral = number
		letters_to_arabic = list()
		arabic_number = 0
		# ======enter code below======
		
		for i in range(0, len(roman_numeral)):
		    if roman_numeral[i] == 'I':
		        letters_to_arabic.append(int(1))
		    elif roman_numeral[i] == 'V':
		        letters_to_arabic.append(int(5))
		    elif roman_numeral[i] == 'X':
		        letters_to_arabic.append(int(10))
		    elif roman_numeral[i] == 'L':
		        letters_to_arabic.append(int(50))
		    elif roman_numeral[i] == 'C':
		        letters_to_arabic.append(int(100))
		    elif roman_numeral[i] == 'D':
		        letters_to_arabic.append(int(500))
		    elif roman_numeral[i] == 'M':
		        letters_to_arabic.append(int(1000))
		print(len(roman_numeral))
		i = 0
		while i < len(letters_to_arabic) - 1:
			if letters_to_arabic[i] < letters_to_arabic[i+1]:
				arabic_number = arabic_number + letters_to_arabic[i+1] - letters_to_arabic[i];
				i = i + 2
			else:
				arabic_number = arabic_number + letters_to_arabic[i]
				i = i + 1

		if i == len(letters_to_arabic):
			if letters_to_arabic[i-2] == letters_to_arabic[i-1]:
				arabic_number = arabic_number + letters_to_arabic[i-1]
		else:
			arabic_number = arabic_number + letters_to_arabic[i]

		# ======enter code above======
		print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result
		return arabic_number 

	else:
		print('Input not valid.')

if __name__ == '__main__':
	input_numerals = ['X', 'XXVIII', 'LXXI', 'XCIX', 'MCMXCIV']
	outputs = [10, 28, 71, 99, 1994]
	results = [True, True, True, True, True]

	for index in range(5):
		if translate_numeral(input_numerals[index]) != outputs[index]:
			results[index] = False

	if False in results:
		print('Not all numerals translated correctly. Try again.')
	else:
		print('Well done! U copied correctly from internet! I am proud! All numerals translated correctly.')

print(translate_numeral("XX"))

