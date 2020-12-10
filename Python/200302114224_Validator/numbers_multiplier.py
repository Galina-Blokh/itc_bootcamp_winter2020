import validator


def numbers_multiplier():
    """
As long as the user provides a wrong input, the function keep telling him/her to provide
    a valid input instead (by printing “Please provide a valid input”).
    :returns print the product of all numbers, entered by user.
"""
    prod = 1
    user_input = input('enter a list of numbers delimited by space')
    while user_input == "" or (not validator.input_validator(user_input)):
        user_input = input('Please provide a valid input')
    list_num = user_input.split()
    for n in list_num:
        prod *= float(n)
    print(prod)


def main():
    """
    Main function of the module, runs functions of the module
    """
    numbers_multiplier()


if __name__ == '__main__':
    main()
    validator.test_input_validator()
    validator.test_is_number()
