'''
multiplier
This function receives a string and returns it with every character mutiplied.
Examples:
 multiplier(“a”) == “aa”
 multiplier(“ab”) == “aabb”
 multiplier("hello world") == "hheelllloo wwoorrlldd"
main
Have a main function, which asks the user to provide a string to multiply.
Print the result of multiplier for the user’s input.
'''

def multiplier(s):
    return ''.join([i for t in zip(s, s) for i in t])
def main():
    s = input('enter the string...')
    print(multiplier(s))

if __name__ == '__main__':
    main()