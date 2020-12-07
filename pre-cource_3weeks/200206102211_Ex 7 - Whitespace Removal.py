'''
Write a function remove_whitespace that removes extra whitespace (spaces, new line, tab)
from the beginning and end of a string. You should implement the functionality on your own
and not use system functions.
After you’ve done that, find a system function that does this for you, and write a new
function remove_whitespace_revised that uses the new function you’ve found.
Submit both versions to
hive.
'''


def remove_whitespace(string):
    import re
    s = re.sub("^\s+|\s+$", "", string, flags=re.UNICODE)
    return s


def remove_whitespace_revised(string):
     return string.strip()
