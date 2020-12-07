'''
Exercise #1
A teacher asked each parent in her class to fill out a row in an MS Excel file,
and write which items of food they
will be bringing to the end-of-the-year party.
She took that column and transfered it to a list called food_list
Then, she wanted to concatenate all of the foods to one string, with a comma between each
food item, so she ran the python command

print(‘, ‘.join(food_list)).

 She got the following error, but she has no numbers in the list:
TypeError: sequence item 0: expected str instance, float found
Google search for the reason why the teacher got this error, and write it down.
 What would you tell the teacher to do in order to avoid the error?
'''
#string.join connects elements inside list of strings
#Use this generator expression instead ‘, ‘.join(food_list):

#food = ','.join(str(v) for v in food_list)
#print(food)
'''
Exercise #2
You are running the following function, that is supposed to create a list with 
the word “hello” in it.
'''
def f(lst=None):
# lst is an optional input and defaults to [] if not specified
    if lst is None:
        lst = []
    lst.append("hello")
    return lst

#You run this function 3 times, and this is the output you get:
print(f())
#[“hello”]
print(f())
#[“hello”, “hello”]
print(f())
#[“hello”, “hello”, “hello”]
'''
But you were expecting to get the same result of [“hello”] every time!
Search Google for what went wrong. How would you change the function for it to work 
as you expect it to?
'''
'''
i will add this code block into function f()
    if lst is None:
        lst = []
__________________________________________
['hello']
['hello']
['hello']

Process finished with exit code 0

'''