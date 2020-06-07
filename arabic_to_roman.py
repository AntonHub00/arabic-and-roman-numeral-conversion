import sys


def arabic_to_roman(user_input):
    try:
        int(user_input)
    except Exception:
        sys.exit('Enter just numbers')

    if int(user_input) > 3999:
        sys.exit('Number most be less than 4000')

    arabic_num = list(user_input)

    # To directly convert arabic digit to roman char depending on if the
    # current digit in the loop is either unit, ten, hundred or thousand.
    units_dict = {'1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
    tens_dict = {'1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'LC'}
    hundreds_dict = {'1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'DM'}
    thousands_dict = {'1':'M', '2':'MM', '3':'MMM'}
    place_values = [units_dict, tens_dict, hundreds_dict, thousands_dict]

    counter = 0
    result = ''

    for digit in arabic_num[::-1]:
        if digit != '0':
            result = place_values[counter][digit] + result
        counter += 1

    return result


if __name__ == '__main__':
    user_input = input("Enter arabic number to convert: ")
    print(arabic_to_roman(user_input))
