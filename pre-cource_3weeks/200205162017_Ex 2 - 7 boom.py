'''
Print all of the numbers between 0 and 100 that are divisible by 7 (without a remainder), or
that contain the number 7, by order.
Use only calculations, loops and 'print'.
'''
for i in range(101):
    if i%7 == 0 or i%10 == 7 or i//10 == 7:
        print(i)