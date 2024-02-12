"""
Write a program that counts the number of vowels in a sound
"""
sentence = input("type sentence")
vowels = ["a", "e", "i", "o", "u" "A", "E", "I", "O", "U"]
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print(count)
