import argparse
import sys

# constant for testing comand_calculator()
NUMBERS = [3, 4, 5, 6, 9, 0]


def add(num1, num2):
    """
    Adds the two numbers
    :param num1:
    :param num2:
    :return: float res of sum of 2 num's
    """
    return num1 + num2


def subtract(num1, num2):
    """
     subtracts the two numbers .
    :param num1:
    :param num2:
    :return: float res of subtraction of 2 num's
    """
    return num1 - num2


def multiply(num1, num2):
    """
    miltiply the two numbers
    :param num1:
    :param num2:
    :return: float res of multiplication of 2 num's
    """
    return num1 * num2


def divide(num1, num2):
    """
    Divides the first number by the second number
    :param num1:
    :param num2:
    :return: float res of division of 2 num's or exeption
    """
    try:
        return num1 / num2
    except:
        return ('you cant divide by 0')


def command_calculator():
    """
      The function  get two numbers and uses them in a simple calculation.
     add – Adds the two numbers and prints the result.

     subtract – Substracts the second number from the first and prints the result.
     divide –  and prints the result.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("operator", choices={"add", "subtract", "multiply", "divide"})
    parser.add_argument("first_number", type=float)
    parser.add_argument("second_number", type=float)
    parser.add_argument("-w", action="store_true", help="show welcome message")

    args = parser.parse_args()

    if args.w:
        print('Good morning!')
    operations = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    print(operations[args.operator](args.first_number, args.second_number))


def test_command_calculator():
    """
    testing the operator functions of command_calculator ()
    """

    assert add(NUMBERS[3], NUMBERS[0]) == 9
    assert subtract(NUMBERS[2], NUMBERS[0]) == 2
    assert multiply(NUMBERS[1], NUMBERS[3]) == 24
    assert divide(NUMBERS[4], NUMBERS[2]) == 1.8
    assert divide(NUMBERS[0], NUMBERS[5]) == 'you cant divide by 0'
    print('tests for function command_calculator()  works correct!')


def main():
    """
    Main function runs  functions of the module
    """
    command_calculator()
    test_command_calculator()


if __name__ == '__main__':
    main()
