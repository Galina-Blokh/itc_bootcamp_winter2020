""" a function  returns a corrected list – where every country’s name begins
with an uppercase letter, and the remaining letters are lowercase, and filters countries
 whose name either begin with ‘i’ or ‘f’, or end with ‘d’ or ‘m’."""


filtered_world_map = (lambda some_list: list(filter(
    lambda my_list: my_list if my_list[0] in ['i', 'I', 'f', 'F'] else my_list[-1] in ['d', 'D', 'm', 'M'],
    list(map(lambda x: x.capitalize(), some_list)))))

countries2 = ['ISRAEL', 'fraNCe', 'engLand', 'BRaZil', 'UkRainE', 'irlAND']
assert filtered_world_map(countries2) == ['Israel', 'France', 'England', 'Irland']

print('filtered_world_map() works correct')
print(filtered_world_map(countries2))
