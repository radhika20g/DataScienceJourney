#Tuple Intialisation
tpl = (1, 2, 3, 4)
print("Tuple: ", tpl)
print('-' * 20)

#Assesing :
print("Printing third element from the tuple: ",tpl[2])
print('-' * 20)

#Slicing
print("Slicing: ", tpl[:2])
print('-' * 20)

#Concatenation
tpl1 = (1,2,3)
tpl2 = (3,4,5)
print("Concatenation: ", tpl1+tpl2)
print('-' * 20) 

#Iterating
print("Iterating elements of tuple: ", tpl)
for i in tpl:
    print(i)
print('-' * 20)

#Checking the element
print("Checking if element exists in tuple:", tpl)
print("3 exists: ", 3 in tpl)
print("9 exists: ", 9 in tpl)
print('-' * 20)

#Checking the frequency of an element:- count(): returns the number of occurrences of a specified element in the tuple.
mytpl = tpl1+tpl2
print(mytpl)
print("Frequency of 3 is:", mytpl.count(3))
print('-' * 20)

#Indexing:- index(element) :  The index method returns the index of the first occurrence of a specified element in the tuple
print("Index of 2: ", mytpl.index(2))
print('-' * 20)

#Multiplying tuple 
tpl = (1,2)
print(tpl*3)
print('-' * 20)

packed_tuple = 1, 2, 'three'

# Tuple packing and unpacking: Tuple packing is the process of placing multiple values in a tuple, while tuple unpacking is the process of extracting values from a tuple.
a, b, c = packed_tuple
print (f" packed Tuple : {packed_tuple}, unpacked tuple a: {a}, b: {b}, c : {c}")
