def translate_day(day):
 translations = {
 "sunday": "Yom Rishon",
 "monday": "Yom Shenee",
 "tuesday": "Yom Shlishee",
 "wednesday": "Yom Revi'ee",
 "thursday": "Yom Chameeshee",
 "friday": "Yom Sheeshee",
 "saturday": "Yom Shabat",
 }
 print(translations[day])
def print_friday_message():
 translate_day("friday")
print_friday_message()



lst = list(range(1, 10))
print(lst)
for i in reversed(range(len(lst))):
    del lst[i]
print (lst)


def is_bird_in_list(lst):
    if "bird" in lst:
        foo = "I found a bird!"
        print(foo)
    else:
        print("No bird in the list")
is_bird_in_list(["boy", "girl", "lady", "dog", "pie"])


message = ""
for number in range(10):
 # use a if the number is a multiple of 3, otherwise use b
 if (number % 3) == 0:
    message = message + "a"
 else:
    message = message + "b"
print(message)