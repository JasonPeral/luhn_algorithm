#The Luhn algorithm is as follows:
    # From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
    # Take the sum of all the digits.
    # If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for x in odd_digits:
        sum_of_odd_digits += int(x)
        print(sum_of_odd_digits)
        sum_of_even_digits = 0

    pass

def main():
    card_number = '4111-1111-4555-1142'

    #Python comes with built in classes where str is one of them which has a method called maketrans that helps us create a translation table
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print(translated_card_number)
    
    verify_card_number(translated_card_number)

main()