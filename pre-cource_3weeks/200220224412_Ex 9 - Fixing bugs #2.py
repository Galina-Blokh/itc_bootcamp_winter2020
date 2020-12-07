'''
List of Zeros
The function is supposed to turn all values in a list to 0. Why is it not working? Fix it. (Hint: read
more about looping through lists)
'''


def to_zeros(lst):
    for item in range(len(lst)):
        lst[item] = 0


lst = [1, 2, 3, 4, 4, 5, 9, 8, 7, 9]
to_zeros(lst)
print(lst)

'''
I, Follow my Js
The following loop prints 10 "j"s followed by an "i", 10 times. But it is not working. Your task is
to fix it.
'''

lst = []
for i in ["j"] * 10:
    for j in ["i"] * 10:
        lst.append(i)
    lst.append(j)

print(lst)

'''
Make me pass!
You had 4 exams, and your average score is Failed. Now, you had new exams and you want to
see if your average improved. You want to make sure you did not Fail anymore 
(Fail is < 60 on average). What is wrong with this code? Fix it
'''

FAILED = True
n_tests = 4
tot_grade = 220
while FAILED:
 grade_str = input("What is the new grade that you got?")
 while not grade_str.isdigit():
    grade_str = input("You did not submit a number. What is your new grade")
 grade_int = int(grade_str)
 n_tests += 1
 tot_grade += grade_int
 print ("Your new average score is: ", round(tot_grade / float(n_tests), 1))
 if round(tot_grade / float(n_tests))<60:
    print("You still Failed")
 else:
    print("You Passed!")
    FAILED = False


'''
Plan my day
Run the following code, that will ask you for the current time (hour), 
and how long you want to stay, and tell you when you will leave. 
After you've seen how it works, run it again, and when asked for what time is it, 
just press OK (Enter). What happened? Fix it.
'''

curr_t_str = input("What time is it now (hour)?")
try:
  curr_t_str = input("What time is it now (hour)?")
  curr_t_int = int(curr_t_str)
  wait_t_str = input("How long do you want to wait (hours)")
  wait_t_int = int(wait_t_str)
  final_t_int = (curr_t_int + wait_t_int) % 24
  print("Yo will leave at: ", final_t_int)
except ValueError:
    print("Input is not a digit: " + curr_t_str)

