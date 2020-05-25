def translate_numeral(number):
        if type(number) == str:  # check type of input
               roman_numeral = 1

                # ======enter code below======
                	arabic_number = "I"


                # ======enter code above======
                print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result
                return arabic_number

        else:
                print('Input not valid.')

if __name__ == '__main__':
        input_numerals = ['I']
        outputs = ['1']
        results = [True]

        for index in range(5):
                if translate_numeral(input_numerals[index]) != outputs[index]:
                        results[index] = False

        if False in results:
                print('Not all numerals translated correctly. Try again.')
        else:
                print('Well done! All numerals translated correctly.')
