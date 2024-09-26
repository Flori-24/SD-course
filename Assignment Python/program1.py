#1. Write a python program to test whether a passed letter is a vowel or not?




p = input("Enter a letter: ")

def is_a_vowel(letter):
    vowels = 'aeiouAEIOU'
    return letter in vowels

if is_a_vowel(p):
    print("{} is a vowel.".format(p))
else:
    print("{} is not a vowel.".format(p))
    
