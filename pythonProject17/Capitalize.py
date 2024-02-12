"""
Write a program that accepts string input, and capitalises the first letter
of each word in the string , and then returns the result string
"""


def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


sentence = input("Enter a sentence: ")
print(capitalize_words(sentence))
