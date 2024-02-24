#Problem Statement - Write a Python program that takes a sentence and count the frequency of each unique word in the sentence.
user_input = input("Enter the sentence: ")

words = user_input.split()
wordCount = {}

for w in words:
    wordCount[w] = wordCount.get(w, 0) + 1

print(wordCount.items())