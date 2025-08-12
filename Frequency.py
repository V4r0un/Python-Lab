from collections import Counter
string = (input("Enter a string = "))
words = string.split()
wordCount = Counter(words)
print(wordCount)