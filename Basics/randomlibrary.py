import random

#what can be add if we want the same random number everytime we run the program
random.seed(2)

#print a random number btw 0.00 to 0.99
print("Random number btw [0,1]:", random.random())

#print a random integer btw 1 to 10
print("Random integer btw [1,10]:", random.randint(1,10))

#choose a random number from the list [1,2,3,4,5]
print("Random number from the list [1,2,3,4,5]:", random.choice([1,2,3,4,5]))

#choose a random sample of 2 from the list [1,2,3,4,5]
print("Random sample of 2 from the list [1,2,3,4,5]:", random.sample([1,2,3,4,5],2))

#print a random float number btw 1.0 and 3.0
print("Random float btw [1,3]:", random.uniform(1.0, 3.0))

