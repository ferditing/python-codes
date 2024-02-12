""""
Write a program that accepts an integer and returns true
if the input is a power of two
"""
def is_power_of_two(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

# Accept user input
num = int(input("Enter an integer: "))
print(is_power_of_two(num))
