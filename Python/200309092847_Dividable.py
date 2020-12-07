import sys

NUMBERS1 = [3, 6, 9, 12]
NUMBERS2 = [3, 6, 9, 13]
DIVIDERS = [3, 7, 5]


def dividable(numbers, divider):
    """
    the one-line function receives 2 list of numbers
     receives a list of numbers and a divisor.
    :return: True if all of the numbers in the list are divisable without a remainder.
    """

    return sum(num % divider == 0 for num in numbers) == len(numbers)


def test_dividable():
    """
    testing function
    :return: confirmation of correct/incorrect work of functions
    """
    assert dividable(NUMBERS1, DIVIDERS[0])
    assert not dividable(NUMBERS2, DIVIDERS[0])

    print("function dividable() works correct")


def main():
    """
    Main function runs  functions of the module
    takes args
    in format like "python dividable.py 6,8,4,2 3"
    """

    numbers = [float(i) for i in sys.argv[1].split(',')]
    divider = float(sys.argv[2])

    test_dividable()
    if dividable(numbers, divider):
        print(str(dividable(numbers, divider)), ': ',
              'all of the numbers in the list are divisable without a remainder')
    elif not dividable(numbers, divider):
        print(str(dividable(numbers, divider)), ': ',
              ' NOT all of the numbers in the list are divisable without a remainder')


if __name__ == "__main__":
    main()
