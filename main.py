#The Luhn algorithm is as follows:
    # From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
    # Take the sum of all the digits.
    # If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'

    #Python comes with built in classes where str is one of them which has a method called maketrans that helps us create a translation table
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    
    verify_card_number(translated_card_number)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()