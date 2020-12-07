WORD = 'hello'

def triple(word):
    """
    one-line function triple that receives a string, and returns another string where
    each character in the original string is tripled.
    :param word: str
    :return: str
    """
    return ''.join([i * 3 for i in word])


def test_triple():
    """
    testing function
    :return: confirmation of correct /incorrect work of functions
    """
    assert triple(WORD) == 'hhheeellllllooo'
    print("function triple() works correct")


def main():
    """
    Main function runs  functions of the module
    """
    test_triple()

if __name__ == "__main__":
    main()
