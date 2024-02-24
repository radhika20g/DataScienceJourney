#string concatenation
print("Radhika" + " Gupta")
print('*'*20)

#string length
print(len('Radhika Gupta'))

#string replication
print('*'*20)

#print a particular character from a string
print('Radhika Gupta'[2])
print('*'*20)

#string slicing
a = 'Radhika Gupta'
print(a[0:8])
print(a[:8])
print(a[8:])
print('*'*20)

#string case coversion 
print('Radhika'.lower())
print('Radhika'.upper())
# Capitalise the first letter of first word only of the string
print('radhika gupta'.capitalize()) 
#capitalise the first letter of each word
print('radhika gupta'.title()) 
print('*'*20)

#string striping - removes extra space from front and end
print('     Radhika Gupta    '.strip())
print('*'*20)

#string replacement
a = "Radhika Gupta"
b = a.replace('a', 'm')
print(b)
print('*'*20)

#string count 
print('Radhika Gupta'.count('a'))
print('*'*20)

#string find
print('find')
print('Radhikakaka Gupta'.find('k'))
print('Radhikakaka Gupta'.index('ka'))
print('*'*20)

#string formating
# Default order 
String1 = "{} {} {}".format('Begineer', 'in', 'Python') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Begineer', 'in', 'Python') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g='Begineer', f='in', l='Python') 
print("\nPrint String in order of Keywords: ") 
print(String1) 