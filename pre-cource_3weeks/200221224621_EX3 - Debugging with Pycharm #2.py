import math


def calculator():
    f_num = float(input('What is the first number? '))
    operation = input('''
What operation would you like to complete? Please enter the wanted option:
===========================
***************************
===========================
+\t\t| addition
-\t\t| subtraction
*\t\t| multiplication
/\t\t| division
sqrt\t| squareroot
pi/\t\t| Divide number with pi
pi*\t\t| Multiply number with pi
fact\t| Factorial calculation of the number
===========================
***************************
===========================

Enter requested operator: ''')

    if operation == 'fact':
        print("{}'s factorial is {}".format(f_num, math.factorial(f_num)))
    elif operation == 'sqrt':
        print('{} square root = '.format(f_num), end='')
        print(math.sqrt(f_num))
    elif operation == 'pi/':
        print('{} / pi = '.format(f_num), end='')
        print(f_num / math.pi)
    elif operation == 'pi*':
        print('{} * pi = '.format(f_num), end='')
        print(f_num * math.pi)
    elif operation in['+','-' ,'*', '/']:
        l_num = float(input('Please enter the second number: '))
        if operation == '+':
            print('{} + {} = '.format(f_num, l_num), end='')
            print(f_num + l_num)
        elif operation == '-':
            print('{} - {} = '.format(f_num, l_num), end='')
            print(f_num - l_num)
        elif operation == '*':
            print('{} * {} = '.format(f_num, l_num), end='')
            print(f_num * l_num)
        elif operation == '/':
            print('{} / {} = '.format(f_num, l_num), end='')
            print(f_num / l_num)
    else:
        print('You have not typed a valid operator, please run the program again.')

    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
ENTER HERE:  ''')

    if calc_again.upper() == 'N':
        print('See you later.')
    elif calc_again.upper() == 'Y':
        calculator()
    else:
        again()


calculator()
