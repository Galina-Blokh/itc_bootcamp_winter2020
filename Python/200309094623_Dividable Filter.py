import sys

NUMBERS1 = [1, 2, 3, 4, 5, 6]
DIVIDERS = [2, 3]


def dividable_filter(numbers, dividers):
    """
        The one-line function receives a list of numbers and a list of divisors.
     :return:  a list
        of all numbers within the given list of numbers, that are
        divisable by at least one divisor from the list of divisors without a remainder.
        """
    return list(set([num for div in dividers for num in numbers if num % div == 0]))


def test_dividable_filter():
    """
    testing function
    :return: confirmation of correct/incorrect work of functions
    """
    assert dividable_filter(NUMBERS1, DIVIDERS) == [2, 3, 4, 6]
    assert type(dividable_filter(NUMBERS1, DIVIDERS)) == list

    print("function dividable_filter() works correct")


def main():
    """
    Main function runs  functions of the module
    takes args
    in format like "python dividable_filter.py 6,0,7,4,2 2,3,5
    """
    test_dividable_filter()

    numbers = [int(i) for i in sys.argv[1].split(',')]
    dividers = [int(i) for i in sys.argv[2].split(',')]

    print(numbers,'and',dividers)
    print((dividable_filter(numbers, dividers)))

if __name__ == "__main__":
    main()
