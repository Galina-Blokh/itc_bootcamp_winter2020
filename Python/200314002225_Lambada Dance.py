import functools

"""Receives two integers – a,b and returns the result of a/b and a%b."""

div_and_mod = lambda a, b: ' you can\'t divide by zero' if b == 0 else (a / b, a % b)

"""Receives one integer – a. If a is negative, returns zero. Otherwise, returns a"""

non_negative = lambda a: a if a >= 0 else 0

"""Receives one integer – a, and returns it with each digit doubled."""

double_digits = lambda a: -double_digits(-a) if a < 0 else int(
    str(a)[0] + functools.reduce(lambda x, y: x + 2 * y, str(a)))

assert div_and_mod(4, 2) == (2.0, 0)
assert div_and_mod(4, 0) == ' you can\'t divide by zero'
assert non_negative(-1) == 0
assert non_negative(1) == 1
assert double_digits(1010) == 11001100
assert double_digits(-1010) == -11001100

print('assertions done')
print(div_and_mod(4, 2), div_and_mod(4, 0))
print(non_negative(-5), non_negative(5))
print(double_digits(13452), double_digits(-13452))
