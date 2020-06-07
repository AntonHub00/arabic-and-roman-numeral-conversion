import sys
from arabic_to_roman import arabic_to_roman


def roman_to_arabic(user_input):
    roman_num = list(user_input)

    if not set(roman_num).issubset({'M', 'D', 'C', 'L', 'X', 'V', 'I'}):
        sys.exit('Available input: M, D, C, L, X, V and I')

    # To check char hierarchy and evaluate string (convert to arabic)
    symbols_weight = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    # Aux to check char hierarchy

    # Gets the last element
    temp_roman_num = roman_num[-1]
    # Gets the arabic num of the last element (unit)
    arabic_num = symbols_weight[temp_roman_num]

    # Iterates from begining to penultimate char, but backwards
    for symbol in roman_num[-2::-1]:
        if symbols_weight[symbol] >= symbols_weight[temp_roman_num[0]]:
            arabic_num += symbols_weight[symbol]
        else:
            arabic_num -= symbols_weight[symbol]

        temp_roman_num = symbol + temp_roman_num

    # If resulting arabic number converted to roman is the same as the input
    # string, then the given number by the user is valid and prints the result
    if arabic_to_roman(str(arabic_num)) == user_input:
        print(arabic_num)
    else:
        sys.exit('Invalid roman number')


if __name__ == '__main__':
    user_input = input("Enter roman number to convert: ")
    roman_to_arabic(user_input)
