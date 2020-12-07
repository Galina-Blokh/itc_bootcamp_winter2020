import copy
from collections import defaultdict

STRING_TO_COUNT = '''Madam President, Mr. Secretary-General, world leaders, ambassadors, and distinguished delegates:
    One year ago, I stood before you for the first time in this grand hall.
    I addressed the threats facing our world, and I
    presented a vision to achieve a brighter future for all of humanity.
    Today, I stand before the United Nations General Assembly to share the extraordinary progress we’ve made.
    In less than two years, my administration has accomplished more than almost any administration in the history of our
    country.'''


def count_char(text):
    """Counts the character frequency in the following text using a default dict.
    :returns a dictionary"""

    d = defaultdict(int)
    for c in ''.join(text):
        d[c] += 1
    return d


def remove_the_keys_grater_5(dictionary_to_clean):
    """Iterate over the dictionary and remove the keys whose values are greater than 5, uses deepcopy
    :returns new dictionary"""
    copy_dict = copy.deepcopy(dictionary_to_clean)
    dout = {k:v for (k,v) in copy_dict.items() if v < 5}
    return dout

def main():
    """ Main function runs and print the output of all  functions  """
    dict_new =count_char(STRING_TO_COUNT)
    print(dict_new)
    clean_dict = remove_the_keys_grater_5(dict_new)
    print(clean_dict)


if __name__ == "__main__":
    main()
