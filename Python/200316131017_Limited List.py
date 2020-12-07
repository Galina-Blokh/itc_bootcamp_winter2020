class LimitedList(object):

    def __init__(self, size_limit):
        """constructor:
        initialized with a maximum number of elements it can hold. """
        self.size_limit = size_limit
        self.list = []
        self.next = 0

    def __getitem__(self, item):
        """get item by index"""
        return self.list[item]

    def __setitem__(self, old_item, new_item):
        """set a new item by index"""
        self.list[old_item] = new_item

    def __iter__(self):
        """iterator for the list the list"""
        for item in self.list:
            yield item

    def __len__(self):
        """:returns the fixed size of the list"""
        return len(self.list)

    def __delitem__(self, index):
        """ delete item by the index"""
        del self.list[index]

    def __repr__(self):
        """evaluable string representation of an LimitedList object"""
        return self.list.__repr__()

    def append(self, item):
        """the filling array with your values function
        After self object has reached its limit, whenever
        someone tries to append an additional value to the list – the new
        member will be appended, and the first member in the list will be erased."""
        if len(self.list) <= (self.size_limit):
            self.list.append(item)
            self.next += 1
            if len(self.list) > self.size_limit:
                self.list.pop(0)


def test_limited_list():
    """testing of limitedList's methods"""
    my_list = LimitedList(3)
    assert str(my_list) == "[]"
    (my_list.append(5))
    assert str(my_list) == "[5]"
    assert (len(my_list)) == 1
    (my_list.append(2))
    assert str(my_list) == "[5, 2]"
    (my_list.append(876))
    assert str(my_list) == "[5, 2, 876]"
    (my_list.append('hgjhf'))
    assert str(my_list) == "[2, 876, 'hgjhf']"
    (my_list.append("7+-/"))
    assert str(my_list) == "[876, 'hgjhf', '7+-/']"
    assert str(my_list[1]) == "hgjhf"
    del my_list[1]
    assert str(my_list) == "[876, '7+-/']"
    print('the LimitedList()works correct ')

def main():
    test_limited_list()


if __name__ == "__main__":
    main()

#
