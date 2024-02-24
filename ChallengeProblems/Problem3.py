#Problem Statement - Count Occurrences of each unique word in a Sentence

def countOccurrences(sentence):
    word_list = sentence.split()
    uniqueWords = []
    word_counts = []

    for word in word_list:
        if word in uniqueWords:
            index = uniqueWords.index(word)
            word_counts[index] += 1
        else: 
            uniqueWords.append(word)
            word_counts.append(1)

    return uniqueWords, word_counts

user_input =  input("Enter the sentence: ")
unique_words, word_counts = countOccurrences(user_input)

print("Word occurrences in the sentence:")
for word, count in zip(unique_words, word_counts):
    print(f"{word}: {count}")