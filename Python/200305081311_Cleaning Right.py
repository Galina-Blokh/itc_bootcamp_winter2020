WORDS = ['hell', 'hello', 'hello worldcofofcfee']

def cleaning_right(words):
    """
    the one-line function receives a list of strings that end with
    randomly ordered ‘c’, ‘o’, ‘f’, ‘e’ letters on the right.
    Note: in case the original string had ends with one of the ‘c’, ‘o’, ‘f’, ‘e’  , the characters cut out
    :return: a new list with the original strings – after cleaning their right edges
    """

    return [word.rstrip('[^cofe]') for word in words]


def test_cleaning_right():
    """
    testing function
    :return: confirmation of correct/incorrect work of functions
    """
    assert cleaning_right(WORDS) == ['hell', 'hell', 'hello world']

    print("function cleaning_right() works correct")


def main():
    """
    Main function runs  functions of the module
    """
    test_cleaning_right()


if __name__ == "__main__":
    main()
