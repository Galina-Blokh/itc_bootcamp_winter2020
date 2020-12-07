WORD = ['hello', 'hello world']


def spaced_triple(word):
    """
    the one-line function space_triple that receives a string, and returns another string where each word in the
    original string is tripled.
    Words are delimited by a space (‘ ‘).

    :return: str with tripled words
    """

    return ' '.join([i * 3 for i in word.split()])


def test_spaced_triple():
    """
    testing function
    :return: confirmation of correct /incorrect work of functions
    """
    assert spaced_triple(WORD[0]) == 'hellohellohello'
    assert spaced_triple(WORD[1]) == 'hellohellohello worldworldworld'
    print("function spaced_triple() works correct")


def main():
    """
    Main function runs  functions of the module
    """
    test_spaced_triple()


if __name__ == "__main__":
    main()
