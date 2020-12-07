NUMBERS1 = [1, 2, 5, 2, 9, 0, 5]
NUMBERS2 = [2, 5, 1, 9, 2]


def ordered_digits(numbers):
    """
        The one-line function receives a list of digits
        Note: we may assume that the input is valid.
     :return:  a string,
            where each digit appears i times,
            where i is the index of the digit in the list (the index starts from one).
        """

    return ''.join([(str(num) * (n + 1)) for n, num in enumerate(numbers)])


def test_ordered_digits():
    """
    testing function
    :return: confirmation of correct/incorrect work of functions
    """
    assert ordered_digits(NUMBERS1) == '1225552222999990000005555555'
    assert type(ordered_digits(NUMBERS1)) == str
    assert ordered_digits(NUMBERS2) == '255111999922222'
    assert type(ordered_digits(NUMBERS2)) == str


print("function ordered_digits() works correct")


def main():
    """
    Main function runs  functions of the module
    """
    test_ordered_digits()


if __name__ == "__main__":
    main()
