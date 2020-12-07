 """ This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Additional basic list exercises """


def remove_adjacent(nums):
    '''
    D. Given a list of numbers, return a list where
all adjacent == elements have been reduced to a single element,
so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
modify the passed in list.

    :param nums:
    :return: list without duplicates
    '''
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i -= 1
        i += 1
    return nums



def linear_merge(sorted1, sorted2):
    '''
    E. Given two lists sorted in increasing order, create and return a merged
list of all the elements in sorted order. You may modify the passed in lists.
Ideally, the solution should work in "linear" time, making a single
pass of both lists.
    :param sorted1:
    :param sorted2:
    :return:  merge sortet list
    '''
    sorted_list = []
    sorted1_index = sorted2_index = 0

    # We use the list lengths often, so its handy to make variables
    sorted1_length, sorted2_length = len(sorted1), len(sorted2)

    for _ in range(sorted1_length + sorted2_length):
        if sorted1_index < sorted1_length and sorted2_index < sorted2_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if sorted1[sorted1_index] <= sorted2[sorted2_index]:
                sorted_list.append(sorted1[sorted1_index])
                sorted1_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(sorted2[sorted2_index])
                sorted2_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif sorted1_index == sorted1_length:
            sorted_list.append(sorted2[sorted2_index])
            sorted2_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif sorted2_index == sorted2_length:
            sorted_list.append(sorted1[sorted1_index])
            sorted1_index += 1

    return sorted_list




def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print("\nremove_adjacent")
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print("\nlinear_merge")
    test(linear_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


if __name__ == "__main__":
    main()
