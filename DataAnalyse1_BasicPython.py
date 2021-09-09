#!/usr/bin/env python
# coding: utf-8

# # Data Analyse

# #  Basic python

# In[3]:


d = {}
l = ()
ll = list()
print({type(d),type(l), type(ll)})


# # Dictionary

# In[4]:


d1 = dict()
l1 = list()
print({type(d1), type(l1)})


# In[6]:


d1 = dict()
d1["apple"] = 100
d1["grape"] = 200
d1


# In[9]:


print(d1["apple"])
print(d1.get("apple"))


# In[13]:


d1["banana"]
d1.get("banana","not found")


# In[20]:


d1.pop("apple")
d1


# In[19]:


del d1["grape"]


# In[25]:


d2 = {'apple': 100, 'grape': 200}
d3 = {'apple': 150, 'banana': 300}
d2.update(d3)
d2


# In[29]:


'apple' in d2


# In[28]:


'tomatoes' in d2


# In[30]:


d2.keys()


# In[31]:


d2.values()


# In[32]:


d2.items()


# # SET

# In[43]:


list1 = [222, 333, 444]
print(type(list1))
set1 = set()
set1 = set(list1)
print(type(set1))
print(set1)
print(list1)


# In[44]:


list2 = [555,'abc', 666,666,'abc']
print(type(list2))
set2 = set(list2)
#print({type(set2[0]),type(set2[1])})
print(set2)


# In[47]:


#create set
'''
   Khác với List - các phần tử có thể giống nhau; Set là tập hợp các phần tử 
   không giống nhau (nếu giống thì nó sữ tự bỏ đi). 
'''
set3 = {1,2,3,4,4,5,5,6,6}
print(type(set3))
print(set3)
#output {1, 2, 3, 4, 5, 6}

# Function of Set
# In[53]:


a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 5, 6}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a-b)


# In[57]:


c = {1, 2, 3, 4, 5}
d = {1, 2, 3}
print(c.issubset(d))
print(c.issuperset(d))
print(c.isdisjoint(d))
print(d <= c)


# In[69]:


e = {'a','b',1, 2, 3, 4}
e.add(5)
print(e)
e.update({5,6,7})
print(e)
e.update(['a','b',8])
print(e)
e.remove(8)
print(e)
e.pop()
print(e)


# # Chú ý về LIST, TUBE, SET
# List: 
# Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it the most powerful tool in Python. The main characteristics of lists are – 
# 
# The list is a datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.
# List are mutable .i.e it can be converted into another data type and can store any data element in it.
# List can store any type of element.
# 
# Tuple: 
# Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. The main characteristics of tuples are – 
# 
# Tuple is an immutable sequence in python.
# It cannot be changed or replaced since it is immutable.
# It is defined under parenthesis().
# Tuples can store any type of element.
# 
# Set: 
# In Python, Set is an unordered collection of data type that is iterable, mutable, and has no duplicate elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. The main characteristics of set are –
# 
# Sets are an unordered collection of elements or unintended collection of items In python.
# Here the order in which the elements are added into the set is not fixed, it can change frequently.
# It is defined under curly braces{}
# Sets are mutable, however, only immutable objects can be stored in it.
# 
# 

# # Assignment mechanism in Python
# Cơ chế gán trong Python

# In[75]:


dog = 100
cat = dog

# cat và dog trỏ tới cùng 1 địa chỉ

print(id(dog))
print(id(cat))
print( dog is cat)
print()

cat = 1999
print(id(dog))
print(id(cat))
print( dog is cat)


# # loop

# In[76]:


e = [2, 3, 4, 5, 6,7, 8, 9]
for i in e:
    if i%2 == 0:
        print(i)
    else:
        continue
    print("{}. It's an even number".format(i))
    


# In[77]:


e = [2, 3, 4, 5, 6,7, 8, 9]
for i in e:
    if i%2 == 0:
        print(i)
    else:
        break
    print("{}. It's an even number".format(i))


# # Modified functions

# In[78]:


# Tham số truyền vào là nhiều
def sum_numbers(a, *b):
    for i in b:
        a += i
    return a


# In[80]:


sum_numbers(1, 2, 3, 4)
    


# In[84]:


def sum_numbers1(a, *b):
    c = 0
    for i in b:
        a += i
        c += 1
    return a,c


# In[85]:


a,c = sum_numbers1(1, 2, 3, 4)
print(a,c)


# In[89]:


def sum_numbers2(a, b):
    for i in b:
        a += i
    return a


# In[92]:


sum_numbers2(1, [2, 3, 4])


# # Scripts and modules in Python
# Viết vào file và chạy từ file

# In[93]:


get_ipython().run_cell_magic('writefile', 'test.py', '\nv_1 = 10\ndef v_add(v_list):\n    c = 0\n    for i in range(len(v_list)):\n        c += v_list[i]\n    return c\n\nl_1 = [1, 2, 3, 4]\nprint(v_add(l_1))')


# In[94]:


get_ipython().run_line_magic('run', 'test.py')


# In[95]:


import test


# In[97]:


test


# In[98]:


print(test.v_1)


# In[99]:


test.v_1 = 30
test.v_1


# In[100]:


l_2 = [20, 30, 40]
test.v_add(l_2)


# In[102]:


import test as ts

ts.v_1


# In[103]:


ts.v_add(l_2)


# In[104]:


from test import v_1, v_add

v_1


# In[105]:


v_add(l_2)


# In[106]:


from test import *


# In[107]:


import os


# In[108]:


os.path.abspath(".")


# In[109]:


os.remove("test.py")


# # ERROR handling

# In[15]:


### import math

for i in range(20):
    try:
        input_n = input("Input a number: ")
        if input_n == "quit":
            break
        r = math.log(float(input_n))
        print(r)
    except ValueError:
        print("input error: value must > 0")
        break
    except Exception:
        print("Unknown error")


# In[115]:


class FirstError(ValueError):
    pass


# In[14]:


l_1 = ["Welcome", "to", "Python"]
while True:
    input_1 = input()
    if input_1 not in l_1:
        raise FirstError("Invalid input")


# In[117]:


try:
    print("try")
finally:
    print("finally")


# In[118]:


try:
    1/0
finally:
    print("this function")


# In[119]:


try:
    1/0
except:
    print("This is exception")
finally:
    print("this function")


# # Read and write file

# In[120]:


get_ipython().run_cell_magic('writefile', 'text.txt', '"hello python"\n"This is a good day for coding"')


# In[130]:


t = open("./files/test.txt")


# In[127]:


t_read = t.read()
print(t_read)
print(type(t_read))


# In[131]:


t_lines = t.readlines()
print(t_lines)
print(type(t_lines))


# In[132]:


for i in t_lines:
    print("current line:",i)
    


# In[133]:


t.close()


# In[140]:


t_2 = open("./files/test_write.txt","w")
t_2.write("This is a good day.\n")
t_2.write("Let's start to learn python.")
t_2.close()


# In[141]:


t_2 = open("./files/test_write.txt","w")
t_2.write("This is a good day.\n")
t_2.write("1234512333\n")
t_2.write("qwerty\n")
t_2.close()


# In[142]:


t_2 = open("./files/test_write.txt","a")
t_2.write("This is a good day.\n")
t_2.write("1234512333\n")
t_2.write("qwerty\n")
t_2.close()


# In[143]:


t_2 = open("./files/test_write.txt","w")
for i in range(15):
    t_2.write(str(i)+"\n")
t_2.close()
t_3 =  open("./files/test_write.txt","r")
print(t_3.read())


# In[146]:


t_2 = open("./files/test_write.txt","w")
try:
    for i in range(100):
        10/(i-50)
        t_2.write(str(i)+"\n")
except Exception:
    print("Unknow error:",i)
finally:
    t_2.close()


# In[151]:


t_3 =  open("./files/test_write.txt","r")
print(t_3.read())


# In[150]:


# More safe: tự try và tự close file khi ko dùng
with open("./files/test_write.txt","w") as f:
    f.write("Hello Python")
    


# # Class

# In[152]:


class Person:
    energy = 1000
    
    def __init__(self, alias, age):
        self.age = age
        self.alias = alias
        
    def display_energy(self):
        print(Person.energy)
        
    def display_alias(self):
        print(self.alias)


# In[153]:


p_1 = Person("Paul", 25)
p_2 = Person("Mark", 28)


# In[154]:


p_1.alias


# In[155]:


p_2.age


# In[156]:


p_2.display_energy()


# In[157]:


del p_2.alias


# In[158]:


p_2.alias


# In[159]:


hasattr(p_1,"age")


# In[160]:


hasattr(p_2,"alias")


# In[162]:


getattr(p_1, "age")
setattr(p_1, "age", 15)
getattr(p_1, "age")


# In[164]:


delattr(p_1,"age")


# # Inheritance of class

# In[181]:


class Parent:
    number = 10
    def __init__(self):
        print("this in the parent class")
        
    def firstFunc(self):
        print("This is the first function of the parent class")
    
    def setAttr(self, attr):
        Parent.parentAttribute = attr
    
    def getAttr(self):
        print("Parent attribute:",Parent.parentAttribute)

class Child(Parent):
    def __init__(self):
        print("this in the child class")
        
    def firstFunc(self):
        print("Changed")
    
    def secondFunc(self):
        print("This is the second function of the child class")


# In[182]:


c_1 = Child()
c_1.firstFunc()
c_1.secondFunc()
c_1.setAttr(200)
c_1.getAttr()


# In[191]:


class Staff:
    def __init__(self):
        self.age = 25
        self.name = "Paul"
        self.salary =  1000
        
    def showData(self):
        print(self.name +" "+str(self.age)+" "+str(self.salary))
        
class Worker(Staff):
        
    def addShift(self, shift):
        self.shift = shift
    
    def showShift(self):
        print(self.shift)
        
    def showData(self):
        super().showData()
        print(self.shift)
    
w_1 = Worker()
w_1.addShift("morning")
w_1.showData()
#w_1.showShift()
                


# # Date and Time management

# In[193]:


import time


# In[195]:


print(time.time())


# In[196]:


print(time.time())


# In[197]:


print(time.localtime(time.time()))


# In[199]:


print(time.asctime(time.localtime(time.time())))


# In[202]:


print(time.strftime("%d-%m-%Y  %H:%M:%S",time.localtime()))


# In[203]:


import calendar


# In[204]:


print(calendar.month(2018,7))


# In[207]:


print(help(calendar.month))


# # Practical exercise Python

# TASK 1:
# We have four numbers 1, 2, 3, 4. We have to create combinations
# made by 3 digits, where each combination must be unique and 
# there cannot be duplicated
# 
# Task: what are the combinations we can get, taking in 
# consideration the condition indicated above?

# In[217]:


s_a = {1, 2, 3, 4}

i = 0
result = []
for a in s_a:
    s_b = s_a.difference({a})
    for b in s_b:
        s_c = s_b.difference({b})
        for c in s_c:
            tmp = a*100 + b*10+ c
            i += 1
            result.append(tmp)          
            
print(result)
print(len(result))
            


# In[218]:


i = 0
for i_1 in range(1,5):
    for i_2 in range(1,5):
        for i_3 in range(1,5):
            if (i_1 != i_2) and (i_1 != i_3) and (i_2 != i_3):
                i += 1
                print (i_1, i_2, i_3)
                
print(i)


# TASK 2:
# The rewards that a company gives to their employees are based on profits. We divide the profits in the following way:
#     1. 1st less or equals to 10.000E, bonus is 10%
#     2. 2nd greater than 10.000E, less than 20.000E, where the 
#     part less than 10.000E will still be 10% and the part which
#     exceeds 10.000E bonus will be 7.5%
#     3. 3rd between 20 and 40, the bonus of the part exceeding
#     20 will be 5%
#     4. 4th between 40 and 60, the bonu of the part exceeding 40
#     will be 3%
#     5. 5th between 60 and 100, the bonu of the part exceeding 60
#     will be 1.5%
#     6. 6th greater than 100, the bonu of the part exceeding 100
#     will be 1.0%
# 
# Task:
#     The monthly profit must be put in and it has to calculate the total import of the bonus

# In[2]:


def bonusCalculator(income):
    profit = [100000, 60000, 40000, 20000, 10000, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for index in range(0, 6):
        if income > profit[index]:
            r += (income - profit[index]) * rate[index]
            income = profit[index]
    return r


# In[3]:


print(bonusCalculator(67000))

TASK 3: 
Create three integer x,y,z

Task: Order the integers from the smallest to the largest
# In[4]:


l1 = [4,3,7]
l1.sort()
print(l1)


# In[18]:


l1 = []
N = 0
while N<3:
    try:
        input_n = int(input("input number:"))
        l1.append(input_n)
        N += 1
    except ValueError:
        print("it must be a number ")
        continue
    except Exception:
        print("Exception")
        continue
        
l1.sort()
#l1.sort(reverse = True)
print(l1)


# TASK 4:
# Insert a line of text and get the number of letters, the numbers of spaces,
# the quantity of numbers, and the quantity of all the remainder from the inserted row

# In[27]:


s1 = "Hoa 1 2 1 hồng nở, hoa hồng lại rụng.\n Hoa tàn hoa nở cũng vô tình.\n"

n_letter = 0
n_space = 0
n_num = 0
n_remainder = 0

for i in range(0, len(s1)):
    if s1[i].isdigit():
        n_num += 1
    elif s1[i].isalpha():
        n_letter += 1
    elif s1[i].isspace():
        n_space += 1
    else:
        n_remainder += 1
       
        
print(n_letter)
print(n_space)
print(n_num)
print(n_remainder)
print (len(s1))


# TASK 5: Devide a list with a comma

# In[31]:


s_1 = " Trần mỹ An, Phan Như Bình, Quỳnh Nhu, Hữu Trọng, Mỹ, Hoài"
l_1 = s_1.split(",")
l_2 = s_1.split(",", 2)
print(l_1)
print(l_2)



# In[38]:


l_1 = ["qwerty","hello",123,456]
#v = ",".join(str(i) for i in l_1)
v = ",".join(str(i) for i in l_1)
print (v)


# In[40]:


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
print(myDict)


# TASK 6:
# Create an anonymous function and to an addition

# In[41]:


v_sum = lambda x,y: x+y
print(v_sum(5,9))


# In[ ]:





# In[ ]:




