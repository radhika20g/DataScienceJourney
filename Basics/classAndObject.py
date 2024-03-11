class person: #creating a class called as person
    name = 'Radhika'
    age = 22

#creating a object p1
p1 = person()
print(p1.name) #printing default name & age 
print(p1.age)
print('-'*50)

p1.name = 'Anuj' #assinging new name and object to object p1
p1.age = 23
print(p1.name)
print(p1.age)
print('-'*50)

#*********************************************************************

class greet:
    name = 'Rads'
    #creating a method inside of a class
    def sayHello(self):  #Self is the instance of class
        print("Hello", self.name)
    
a1 = greet()
a1.sayHello()

#*********************************************************************

class mathematics:
    def factorial(self, n):
        s = 1
        for i in range(1, n+1):
            s*= i
        return s
    
    def lst_multiply(self, lst):
        s = 1
        for i in lst:
            s*= i
        return s
    
    def dot_multiply(self, lst1, lst2):
        return[lst1[i]*lst2[i] for i in range(len(lst1))]
    
m1 = mathematics()
print("Factorial of 5:", m1.factorial(5))
print("List Multiplication [1,2,3,4,5]:", m1.lst_multiply([1,2,3,4,5]))
print("List dot multiplication btw [1,2,3] and [2,3,4]:", m1.dot_multiply([1,2,3], [2,3,4]))
print("-"*30)

#*********************************************************************
#__init__ method for intializing / Constructors 
class greet:
    def __init__(self, name, sirname):
        self.name = name
        self.sirname = sirname
    
    def sayHello(self):
        print("Hello", self.name)

p1 = greet("Radhika", "Gupta")
p1.sayHello()