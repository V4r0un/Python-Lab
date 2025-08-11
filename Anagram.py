from collections import Counter
string1 = (input("Enter first string = "))
string2 = (input("Enter second string = "))

if len(string1) != len(string2):
    print("It is not an Anagram character")
else:
    if Counter(string1) == Counter(string2):
        print("It is an Anagram character")
    else:
        print("It is not an Anagram character")
        