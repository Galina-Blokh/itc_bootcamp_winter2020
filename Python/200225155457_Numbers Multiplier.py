'''
Ask the user to provide a list of numbers delimited by space (‘ ‘).
Then, print the product of all numbers.
Examples:
If the user provides ‘1 2 3’, print 6.
If the user provides ‘0 500 12 5’, print 0.
If the user provides ’12 4 5’, print 240.
If the user provides ‘5’, print 5.
You may assume that the input is valid – that is, the user has only inserted integers
delimited by a space.
'''
#


def main():
    a = []
    try:
        a = [int(i) for i in input('enter a list of numbers delimited by space').split()]
    except:
        print('Error: only numbers, pls., delimited by space!!!!')
    prod = 1;
    for n in a:
        prod *= n
    print(prod)


if __name__ == '__main__':
    main()