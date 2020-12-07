class WickedDictionary(object):
    """a class called WickedDictionary, that will act like a normal dictionary,
 except for one thing: whenever someone
creates a new key, that key will be doubled."""

    def __init__(self, init=None):
        """constructor"""
        if init is not None:
            self.__dict__.update(init)

    def __getitem__(self, key):
        """get item by the key"""
        return self.__dict__[key]

    def __setitem__(self, key, value):
        """whenever someone
            creates a new key, that key will be doubled."""
        self.__dict__[key * 2] = value

    def __delitem__(self, key):
        """ delete item by the key"""
        del self.__dict__[key]

    def __contains__(self, key):
        """returns true/false if the key is in dictionary"""
        return key in self.__dict__

    def __len__(self):
        """:returns the length of the dictionary"""
        return len(self.__dict__)

    def __repr__(self):
        """evaluatable string representation of an LimitedList object"""
        return repr(self.__dict__)


def test_wicked_dict():
    """testing of WickedDictionary methods"""
    my_dict = WickedDictionary()
    my_dict['hello'] = 12
    my_dict[2] = "test"
    assert my_dict[4] == 'test'
    assert str(my_dict) == "{'hellohello': 12, 4: 'test'}"
    print('WickedDictionary works correct ')


def main():
    test_wicked_dict()


if __name__ == "__main__":
    main()
