'''
 the title should have every word start with an uppercase letter, and the other characters should
be lowercase.
 In addition, the title string has a minimum length, and if it’s not reached – then the title must be padded
with zeros to its left.

This function receives a string, and a pad width, and encodes the string as a title
(according to the instructions provided above).
Note: for every word, the first alphabetic character has to be uppercase.
For instance, if the word is ‘123abc’, then it will
be encoded as ‘123Abc’.
Examples:
 encode_title("aaaa", 4) == "Aaaa"
 encode_title("aaaa", 5) == "0Aaaa"
 encode_title("hello mY naME is iynigo Montoya", 40) == '000000000Hello My Name Is Iynigo Montoya'
 encode_title("000hello mY naME is iynigo Montoya", 40) == '000000000Hello My Name Is Iynigo Montoya'
main
Have a main function, which asks the user (the reporter) to provide a string to encode,
as well as the minimum length of the string.
Print the result of encode_title for the user’s use
'''
def encode_title(stri, lenth_stri):
    return stri.title().zfill(lenth_stri)

def main():
    title_string = input("enter the title to encode:\n")
    lenth_of_str = int(input('the minimum length of the string:\n'))
    print(encode_title(title_string,lenth_of_str))

if __name__ == '__main__':
    main()