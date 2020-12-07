import sys

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print('the numbers themselves are:', num1, num2)
    print('the sum of digits is:', num1 + num2)
    print('the difference between the numbers:', num1 - num2)
    print('the product of the numbers is:', num1 * num2)

'''
gal@gal-VirtualBox:~/PycharmProjects/untitled$ python using_command_line_arguments.py 5 4
the numbers themselves are: 5 4
the sum of digits is: 9
the difference between the numbers: 1
the product of the numbers is: 20
'''


