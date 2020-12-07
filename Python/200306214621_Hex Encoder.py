MSG = ["hello world", 'a', 'aaa']
NUM_Z = 2


def hex_encoder(msg):
    """
        The one-line function receives  a string

     :return:  this string Hex-encoded
        """

    return ''.join([hex(ord(l))[NUM_Z:].zfill(NUM_Z) for l in msg])


def test_hex_encoder():
    """
    testing function
    :return: confirmation of correct/incorrect work of functions
    """
    assert hex_encoder(MSG[0]) == '68656c6c6f20776f726c64'
    assert hex_encoder(MSG[1]) == '61'
    assert hex_encoder(MSG[2]) == '616161'
    assert type(hex_encoder(MSG[0])) == str
    assert type(hex_encoder(MSG[1])) == str
    assert type(hex_encoder(MSG[2])) == str


print("function hex_encoder() works correct")


def main():
    """
    Main function runs  functions of the module
    """
    test_hex_encoder()


if __name__ == "__main__":
    main()
