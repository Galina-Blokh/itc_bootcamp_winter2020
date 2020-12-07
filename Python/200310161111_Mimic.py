#!/usr/bin/python -tt
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.
"""

import random
import sys

PATH = 'alice_mimic.txt'
NUMBER_OF_WORDS = 200
NUMBER_OF_ARGS = 2
FILE_NAME = 1


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    mimic_dict = {}
    prev = ''
    try:
        with open(filename, 'r+') as file:
            data = [line.strip().split() for line in file]
            for line in data:
                for word in line:
                    if not prev in mimic_dict:
                        mimic_dict[prev] = [word.strip()]
                    else:
                        mimic_dict[prev].append(word.strip())
                    prev = word
        return mimic_dict
    except:
        sys.exit("can't read a file")


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    try:

        for num in range(NUMBER_OF_WORDS):
            print(word)
            next_word = mimic_dict.get(word)
            if not next_word:
                next_word = mimic_dict['']
            word = random.choice(next_word)
    except:
        sys.exit('something went wrong :(')

def test_mimic_dict():
    """
    testing the mimic_dict() function
    """
    assert type(mimic_dict(PATH)) == dict
    print('testing function mimic_dict() passed!')

def main():
    """ Provided main(), calls print_mimic and mimic() and get user's input: filename.txt """
    test_mimic_dict()
    if len(sys.argv) != NUMBER_OF_ARGS:
        print('usage: ./mimic.py file-to-read')
        sys.exit(FILE_NAME)

    my_dict = mimic_dict(sys.argv[FILE_NAME])
    print_mimic(my_dict, '')



if __name__ == "__main__":
    main()