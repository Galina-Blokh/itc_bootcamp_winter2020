def zipper(elements1, elements2):
    """
    The function receives two elements – each of them is either a list or a tuple.
    :return: a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or
            iterables. The returned list’s length is equal to the length of the shorter argument the function receives.
    """
    result = []
    result_length = 0
    if len(elements1) < len(elements2):
        result_length = len(elements1)
    else:
        result_length = len(elements2)
    for i in range(result_length):
        result.append((elements1[i], elements2[i]))
    return result


def main():
    """ main() calls the above functions with interesting inputs,
        using assert to check if each result is correct or not. """
    assert zipper([1, 2, 3], [4, 5, 6]) == [(1, 4), (2, 5), (3, 6)]
    assert zipper([1, "hello world"], [4, 5, 6, 7, 8, 9]) == [(1, 4), ('hello world', 5)]



if __name__ == '__main__':
    main()
