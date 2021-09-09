#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")


# In[3]:


x = 5
print(x)
x = "Global"
print(x)


# In[6]:


def print_func():
    print("Print a string inside a function")
def print_funcX(x):
    print("x is inside:",x)


# In[7]:


print_func()
print_funcX(5)


# In[16]:


# String 
x = "Hello"
print(x)
print("Up case")
print(x.upper())
print(x.lower())
print(len(x))
print(x.replace("l","a"))
print("enter your name")
x = input()
print("hello,"+ x)


# In[25]:


# OPERATOR

x = 30
y = 20
z = x * y
print(x + y)
print(x - y)
print (z)
print(int(y/x))
print(x%y)


# In[29]:


#Comparison operator
x = 10
y = 20
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# In[30]:


#STRING
x = "Programming"
print(x.upper())
print(x.lower())
print(len(x))
print(x.replace("m","a"))


# In[46]:


# assignment
x = 8
print(x)
x += 1
print(x)
x -= 2
print(x)
x *= 2
print(x)
x %= 3
print(x)
x = 8
x //= 3
print(x)

x = 2
x **= 3
print(x)
x = 8
x//=3
print(x)


# In[49]:


# membership opperator
lista = [5, 10, 6]
listb = [2,4,6]
for item in lista:
    if item in listb:
        print("coincide")
    else:
        print("Not coincide")

for item in lista:
    if item not in listb:
        print("NOT coincide")
    else:
        print("coincide")


# In[1]:


# Variable
"""
    Multiline comment
""" 
    

Variable_1 = 7
Variable_1 = 9
print(str(Variable_1))

float_1 = 1.0
int_1 = 1
bool_1 = True
hold_type = [type(float_1), type(int_1), type(bool_1)]
print(str(hold_type))


# In[10]:


#Comment and Math Operators
print(str([int(120 / 2 * 6 + 19),int(25 % 3 + 17 / 5 * 10),int(5 / 2 % 4 * 6 ** 3)]))

# PRINT
print(5+6)


# In[14]:


# for more float
ex1 = 1.23 + 4.56
ex2 = 123 + 456

print(ex1)
print(ex1/100)
print(str(3.09 - 4.12))
print(str((3.09 * 100 - 4.12 * 100) / 100))


# In[18]:


#String
str1 = "example"
ex1 = str1[0]
print(ex1)
ex2 = "tape"[2]
print(ex2)

example = "apples"
ex1 = example[:3]
print(ex1)
ex2 = example[2:5]
print(ex2)
ex3 = example[3:]
print(ex3)
ex4 = "apples"[:3]
print(ex4)
ex5 = "apples"[2:5]
print(ex5)
ex6 = "apples"[3:]
print(ex6)

print("word1 " + "word2 " + "word3")
to_print = "R2" + "-D2"
print(to_print)


# In[25]:


# str() va int()
ex1 = True
ex2 = 5
ex3 = 3.21
converted = str(ex1)
print(converted)
print(str(ex2))
print(str(ex3)[1])

ex4 = "123"
ex5 = "9.4"
converted = int(ex4)
print(converted)
#print(int(ex5))
print(int(9.4))
var1 = 1
var2 = "2"
var3 =  str(var1)
var4 = int(var2)
print(str([type(var3),type(var4)]))


# In[29]:


#.format
name1 = "John Smith"
age1 = 36
occupation1 = "tax attorney"
city1 = "New York"

name2 = "Elizabeth Yates"
age2 = 25
occupation2 = "junior IOS developer"
city2 = "Denver"

string1 = "{} is a {} year old {} living in {}"
string2 = "{3} is the city {1} year old {2} {0} calls home"
print(string1.format(name1,age1,occupation1,city1))
print(string1.format(name2,age2,occupation2,city2))
print(string2.format(name1,age1,occupation1,city1))
print(string2.format(name2,age2,occupation2,city2))


# In[2]:


# FUCNTION
input1 = 20
input2 = 50
added_int = 30
def product(a = 10, b = 40):
    return(a * b)
output1 = product(input1, input2) + added_int
print(product())
print(output1)


# In[6]:


import math
from fractions import Fraction
print(math.sqrt(4))
print(float(Fraction(1,2)))
print(abs(-9))
print(type("apple"))
print(max(5,7,1,4,3))
print(min(5,7,1,4,3))


# In[13]:


toBeChanged = [3, 5, 6, 7, 8, 10, 8, 7, 6, 5, 3]
print(toBeChanged[5])
toBeChanged[2] = 4
print(toBeChanged)
toBeChanged.append(11)
print(toBeChanged)
print(toBeChanged.index(len(toBeChanged) - 1))
toBeChanged.insert(11, 2)
print(toBeChanged)
toBeChanged.remove(10)
print(toBeChanged)
print(toBeChanged.pop(-1))
print(toBeChanged)
print(toBeChanged[-1])
toBeChanged.remove(7)
print(toBeChanged)


# In[14]:


descend_ascend = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(descend_ascend[:5])
print(descend_ascend[2:7])
print(descend_ascend[4:])
print(descend_ascend[1:8:2])


# In[15]:


ex_tuple = (1, 2, 3, 4, 5)
print(ex_tuple[3])
print(ex_tuple[::2])


# In[21]:


planets = {0: "Sun", 1: "Mercury", 2: "Veenus", 3: "Earth"}
print(planets[3])
planets[4] = "Mars"
print(planets)
print(len(planets))
planets[2] = "Venus"
print(planets)
del(planets[0])
print(planets)


# In[25]:


# For loop
the_str = "orange"
the_list = [5, 4, 3, 2, 1, 0]
the_tuple = (1, 6, 2)
for item in the_str:
    print(item, end = "")
print()
for item in the_list:
    print(item, end = "")
print()
for item in the_tuple:
    print(item, end = "")


# In[26]:


counter = 0
while counter <= 3:
    print("counter"+str(counter))
    counter += 1
else:
    print("The loop has ended")


# In[34]:


# RANGE 
ex1 = range(8)
for num in ex1:
 print(num)
#ex1 = range(8)
print(ex1)
ex2 = list(ex1)
print(ex2)
print([type(ex1), type(ex2)])

ex3 = list(range(1, 4))
print(ex3)

ex4 = list(range(2, 20, 3))
print(ex4)


# In[38]:



ex1 = list(range(10))
print(ex1)
ex2 = list(range(5,10))
print(ex2)
ex3 = list(range(1,48,2))
print(ex3)


# In[46]:


ex1 = [num**2 for num in range(1,6)]
print(ex1)

input2 = [1, -2, 3, -4, 5, -6]
ex2 = [num for num in input2 if num > 0]
print(ex2)

input2 = [[1, 2, 3], "apricot", 3.12, 101, [6,5, 4], True, (7, 2, 6, 4), False, "Pineapple", range(4)]
ex3 = [item for item in input2 if type(item)in [type(True), type([1, 2, 3])]]
print(ex3)


# In[49]:


# OOP BASIC
# create an object
class AutoMobile:
    fuel = "gas"
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost


# In[51]:


Civic = AutoMobile("Honda", 18740)
#accessing attributes of objects
print(Civic.brand)
print(Civic.cost)


# In[52]:



#giving an object a new attribute
Taurus = AutoMobile("Ford", 27345)
print(Taurus.brand)
print(Taurus.cost)
Taurus.color = "red"
print(Taurus.color)


# In[53]:


# The class “AutoMobile” and the objects “Civic” and “Taurus” all have the attribute “fuel”
print(AutoMobile.fuel)
print(Civic.fuel)
print(Taurus.fuel)


# In[54]:


# reassigning object attributes

Civic.brand = "Toyota"
print(Civic.brand)


# In[56]:


# reassigning an attribute that belongs 
#to an instance of a class
print(Taurus.color)
Taurus.color = "blue"
print(Taurus.color)


# In[58]:


class AirCraft:
    moving = "passengers"
    def __init__(self, cruising_speed, lenght):
        self.cruising_speed = cruising_speed
        self.lenght = lenght

Boeing_737 = AirCraft(583, 110)
print(Boeing_737.cruising_speed)
print(Boeing_737.lenght)
Boeing_737.airline = "Delta Air Lines"
print(Boeing_737.airline)

print(AirCraft.moving)
print(Boeing_737.moving)

Boeing_737.lenght = 116
print(Boeing_737.lenght)

Boeing_737.airline = "Alaskan Airlines"
print(Boeing_737.airline)

AirCraft.moving = "cargo"

print(AirCraft.moving)
print(Boeing_737.moving)


# In[67]:


class Batman:
    def __init__(self, hero_name):
        self.hero_name = hero_name
    def is_real(self, real_name):
        if real_name == "Bruce Wanye":
            return True
        else:
            return False
    def uses_function(self, name_entered):
        if self.is_real(name_entered):
            return "Yes, Bruce Wayne is {}".format(hero_name)
        else:
            return "No, {} is not Batman's secret identity". format(name_entered)
        
guess1 = Batman("Batman").uses_function("Bruce Wayne")
print(guess1)

guess2 = Batman("The Caped Crusader")
print(guess2.is_real("Christian Bale"))
print(guess2.uses_function("Harvey Dent"))


# In[65]:


class ExpensiveFruit:
    def __init__ (self, name):
        self.name = name
    def total_price(self,cost, quantity):
        output1 = "The total cost of your {} purchase is ${}.".format(self.name,cost * quantity) 
        return (output1)
        
total1 = ExpensiveFruit("Dekopon").total_price(13,6)
print(total1)

fruit2 = ExpensiveFruit("Mangosteen")
print(fruit2.total_price(10,4))
    


# In[70]:


# Inheritance

class AutoMobile:
    def __init__ (self, brand, cost):
        self.brand = brand
        self.cost = cost
    
class SportsCar(AutoMobile):
    doors = 2
    seats = 2

class Truck(AutoMobile):
    fuel = "diesel"
    
Aventador = SportsCar("Lamborghini", 399500)
print(Aventador.brand)
print(Aventador.cost)
print(Aventador.doors)
print(Aventador.seats)

Ram_1500 = Truck("Dodge", 27095)
print(Ram_1500.brand)
print(Ram_1500.cost)
print(Ram_1500.fuel)


# In[71]:


class Mammals:
    def __init__(self, movement):
        self.movement = movement
        
class Humans(Mammals):
    communication = "talking"

class Whales(Mammals):
    sonar = "echolocation"
    
people = Humans("walking")
print(people.movement)
print(people.communication)

whale = Whales("swimming")
print(whale.movement)
print(whale.sonar)


# In[72]:


print(len("Hello World"))

print("Hello World".lower())


# In[ ]:




