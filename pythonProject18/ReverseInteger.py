"""
Write a program that takes integer as input and return the
integer with reversed digit ordering
"""


def reverse_integer(number):
    sign = -1 if number < 0 else 1
    reversed_number = sign * int(str(abs(number))[::-1])
    return reversed_number

number = int(input("Enter an integer: "))
print(reverse_integer(number))
