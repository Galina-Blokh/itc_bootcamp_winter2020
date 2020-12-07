'''
Exercise 1
Get as input details about two different people: ask for their name, age, height and weight, of
a person, and print the following format, per person (one line per person): "Name: <name>,
Age: <age>, BMI <bmi calculation>". You need to fill the <> in your code.
'''

person = dict()
person2 = dict()
name = input('enter your name: ')
height = float(input('enter your height: '))
weight = float(input('enter your weight: '))
bmi = format(weight/height**2,'.2f')

person1.update(Name = name, Height = height, BMI = bmi)
print(person1)
#enter your name: Nick
#enter your height: 2.02
#enter your weight: 89
#{'name': 'Nick', 'height': 2.02, 'bmi': '21.08'}

person2.update(Name = name, Height = height, BMI = bmi)
print(person2)
#enter your name: Olga
#enter your height: 1.68
#enter your weight: 80
#{'name': 'Olga', 'height': 1.68, 'bmi': '19.61'}

'''
Exercise 2
In your previous code, you might have repeated some code. use loops so that each row will
only be used once.
'''

n = 2
person = dict()
while n > 0:
    name = input('enter your name: ')
    height = float(input('enter your height: '))
    weight = float(input('enter your weight: '))
    bmi = format(weight / height ** 2, '.2f')
    person.update(Name=name, Height=height, BMI=bmi)
    print(person)
    n -= 1

'''
Exercise 3
Let's focus on the BMI Calculation. Create a function def calculate_bmi(weight,
height) that will calculate the BMI, and change your code so it uses it. Creating functions
help us organize our code better, and make changes to the calculation in one place only,
instead of fixing it all through the code.
'''

def calculate_bmi(weight,height):
    bmi = format(weight / height ** 2, '.2f')
    return bmi

n = 2
person = dict()
while n > 0:
    name = input('enter your name: ')
    height = float(input('enter your height: '))
    weight = float(input('enter your weight: '))
    person.update(Name=name, Height=height, BMI=calculate_bmi(weight,height))
    print(person)
    n -= 1

'''
Exercise 4
BMI calculation, is relevant to humans. We would like to calculate this value only if we are
given data about a person. A useful way to do it, is to create a new data structure using 
Class in python, that will store the data we know about a person, and contain all the 
functions that are only relevant to humans. Construct Class Person, with a constructor,
 and a modified version of your calculate_bmi(weight, height) function, which will now
  be a Class method. After you build the class, get all the needed parameters 
  (the ones you had in the beginning of the exercise), create an instance of a person, 
  and print his BMI.
'''


class Person(object):
    '''
    Class Person, with a constructor,
 and a modified version of calculate_bmi(weight, height) method
    '''

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return format(self.weight / self.height ** 2, '.2f')


if __name__ == "__main__":
    girl = Person('Galina', 1.72, 62)
    boy = Person('Ali', 1.77, 88)
    print('girls BMI is', girl.calculate_bmi())
    print('boys BMI is', boy.calculate_bmi())
