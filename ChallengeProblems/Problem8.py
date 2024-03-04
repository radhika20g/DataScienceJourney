#Problem Statement - Dictionary Comprehension - Find Common Elements from the given multiple Lists.

def find_common_elements(lists):
    common_ele = {element: min(lst.count(element) for lst in lists) for element in set.intersection(*map(set, lists))}
    return common_ele

list1 = [1, 1, 2, 3, 4]
list2 = [2, 2, 3, 4]
list3 = [1, 2, 3, 3]

results = find_common_elements([list1, list2, list3])

for element, frequency in results.items():
    print(f"Element:{element}, Frequency:{frequency}")