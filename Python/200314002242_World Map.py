
""" a function  returns a corrected list – where every country’s name begins with an
uppercase letter, and the remaining letters are lowercase"""

countries = ['ISRAEL', 'france', 'engLand']
world_map = lambda some_list: list(map(lambda x: x.capitalize(), some_list))

assert world_map(countries) == ['Israel', 'France', 'England']
print('world_map() works correct')


