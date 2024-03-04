#Problem Statement- Set and Tuple - Longest Substring Without Repeating Characters
def length_of_longest_substring(str):
    char_set = set()
    max_length = 0
    left_pointer = 0
     
    for right_pointer in range(len(str)):
        while str[right_pointer] in char_set:
            char_set.remove(str[left_pointer])
            left_pointer += 1
        char_set.add(str[right_pointer])
        max_length = max(max_length, right_pointer - left_pointer + 1)

    return max_length

input_str = "abcabcbb"
result = length_of_longest_substring(input_str)
print("Length of Longest Substring:", result)