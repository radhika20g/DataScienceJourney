
my_set = {1,2,3}
print(my_set)
print(type(my_set))
print('*'*20)

#Adding - add(): adds a single element to the set
print(my_set)
my_set.add(4)
print("After adding 4 to set: ", my_set)
print('*'*20)

#Updating - update()- adds multiple element to the set
print(my_set)
my_set.update([5,6,7])
print("After adding 5,6,7 to set: ", my_set)
print('*'*20)

#Popping: Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
print(my_set)
ele = my_set.pop()
print("Popped Element", ele)
print("After poping 1 from set: ",my_set)
print('*'*20)

#Removing: Raises error if element does not exists
print(my_set)
my_set.remove(5)
print("After Removing 5 from set: ", my_set)
print('*'*20)

#Discarding: Does not raise an error if element does not exists
print(my_set)
my_set.discard(2)
print("After Removing 2 from set: ", my_set)
print('*'*20)

#Iterating
print(my_set)
print("Iterating elements of the set")
for i in my_set:
    print(i)
print('*'*20)

#Check if a value is present in a set or not
print(my_set)
print("Checking if 3 exits in set:" , 3 in my_set)
print('*'*20)

#Set Operations
set1 = {1,2,3,4}
set2 = {3,4,5,6}

#Union: Returns a new set containing all unique elements from both sets.
print("Union of set1 and set2: ", set1 | set2)
print('*'*20)

#Intersection: Returns a new set containing common elements between two sets.
print("Intersection of set1 and set2: ", set1&set2)
print('*'*20) 

#Difference: Returns a new set with elements in the first set but not in the second set.
print("Difference (unique elements in set1): ", set1-set2)
print("Difference (unique elements in set2): ", set2-set1)
print('*'*20)

#Symmetric Difference: Returns a new set with elements in either set, but not both.
print("Symmetric Unique Elements: ", set1^set2)
print('*'*20)

#Clearing: Removes all elements from the set, making it empty.
print(set1)
set1.clear()
print(set1)
print('*'*20)

#Copy: copy(): Returns a shallow copy of the set.
set1 = {2,4,5,7,9}
print("Original set: ", set1)
setCopy = set1.copy()
print("Copy set: ", setCopy)
print('*'*20)

#Length: len(): Returns the number of elements in the set.
print("Length of set: ", len(set1))
print('*'*20)