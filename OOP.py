#!/usr/bin/env python
# coding: utf-8

# OOP
# Encapsulatio: attribute + method
# Abstraction: provide essential information
# Inheritance: allow us to add more information
# Polymorphism: poly(many) + form: ability of an object to take
#         on many forms
# 

# In[4]:


# Implementing Classes and Objects
class Employee:
    name = "Paul"
    age = 25
    salary = 100000
    
    def getSalary(self):
        return self.salary

paul = Employee()
print(paul.getSalary())
print(paul.age)


# In[6]:


# Instance Attribute and Class Attribute

class Employee:
    companyName = "ABC"
    
    name = "Paul"
    age = 25
    salary = 100000
    
paul = Employee()
christ = Employee()
paul.companyName = "XYZ"

print("---Paul---")
print(paul.companyName)
print(paul.name)

print("---Christ---")
print(christ.companyName)
print(christ.name)
    


# In[7]:


class Employee:

    #This is class attribute
    companyName = "ABC LLC"

    #These are instance attributes
    name = "Chris"
    age = 29
    salary = 5000


chris = Employee()
paul  = Employee()

print(chris.companyName)
print(paul.companyName)

paul.companyName = "XYZ LLC"

print(paul.companyName)
print(chris.companyName)


# In[13]:


# instant method & static method
class Employee:
    #class atribute
    companyName = "ABC"
    
    #using instance attributes here
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    #Instance Methods
    def showEmployeeDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Company Name:", self.companyName)
        
    def showTest():
        print("Helloooooo")
        
   
    @staticmethod
    def getCompanyInfo():
        print("This company was founded in early days of 2015. Welcome to this company")
        

paul = Employee("Paul", 25, 5000)
paul.showEmployeeDetails()
Employee.getCompanyInfo()

Employee.companyName = "XYZ"
Employee.showTest()


# In[17]:


#init method
paul =  Employee("Paul", 25, 5000)
christ =  Employee("Christ", 30, 7000)
paul.showEmployeeDetails()
Employee.showEmployeeDetails(christ)


# In[20]:


class NewEmployee:
    def newEmployeeData(self):
        self.name = "Tatha"
        age = 25
        print("name: ",self.name)
        print("age:", age)
    
    def getSalary(self):
        self.salary = 50
        print("salary",self.salary)
    
ann = NewEmployee()
ann.newEmployeeData()
ann.getSalary()

print("----")
print(ann.name)
print(ann.salary)


# In[2]:


#Encapsulation and Abstraction
class BMI:
    def calculateBMI(self):
        print("Enter your weight in KG:")
        self.weight = float(input())
        print("Enter your height in Meters:")
        self.height =  float(input())
        
        self.bmi = self.weight /(self.height * self.height)
        
        print("Your BMI is: ",self.bmi)
        
        if self.bmi < 18.5:
            print("You are underweight")
        elif self.bmi > 18.5 and self.bmi < 24.9:
            print("You are healthy")
        elif self.bmi > 24.9 and self.bmi < 29.9:
            print("You are overweight")
        elif self.bmi > 30:
            print("You are Obese")

bmi = BMI()

while True:
    print("1. Calculate Your BMI")
    print("2. Exit")
    
    choice = int(input())
    
    if choice is 1:
        bmi.calculateBMI()
    elif choice is 2:
        break


# In[3]:


#single Inheritance
class Person:
    def setData(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher(Person):
    def __init__(self, salary):
        self.salary = salary
        
    def showTeacherData(self):
        print(self.name,end = " ")
        print(self.age, end = " ")
        print(self.gender, end = " ")
        print(self.salary)
        
teacher = Teacher(9000)
teacher.setData("Bob", 30, "Male")
teacher.showTeacherData()


# In[5]:


# Multilevel Inheritance
class Person:
    name = "Bob"
    age = 40
    gender = "Male"
    
class Student(Person):
    fees = 15000

class TA(Student):
    salary = 5000
    
    def showTaData(self):
        print(self.name,end = " ")
        print(self.age, end = " ")
        print(self.gender, end = " ")
        print(self.fees, end = " ")
        print(self.salary)
        
ta = TA()
ta.showTaData()


# In[8]:


#multiple inheritance
class Person:
    name = "Bob"
    gender = "Male"
    
class Student(Person):
    fee = 5000
    age = 30
    
class Faculty(Person):
    lunch = False
    bonus = True
    age = 40

class TA(Faculty, Student):
    def showTaData(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.fee)
        print(self.lunch)
        print(self.bonus)
        
ta = TA()
ta.showTaData()


# In[5]:


# Public, Protect, private
# Public: can be accessed anywhere in programs
# Protect: can be accessed only in classes and their child classes in programs
'''
    chỉ có thể truy cập trong class khởi tạo nó và class kế thừa từ class đó (class con)
    mà chúng ta sẽ không thể gọi được khi đứng từ bên ngoài class.
'''
# Private:can be accessed only in the class
'''
    chỉ có phạm vi hoạt động ở trong class khai báo nó
'''

class Employee:
    name = "Paul" #Public member
    _age = 30 #Protect member
    __salary = 5000 #Private member
    
    def showEmployee(self):
        print("----",self.__salary)
    
class Test(Employee):
    def showData(self):
        print("Age:", self._age)
        self.showEmployee()

employee = Employee()
print(employee.name)
employee.showEmployee()

test = Test()
print(test.name)

print(test.showData())



# In[7]:


#Polymorphism
'''
define methods in the child class with the same name as defined
in their parent class
'''
class Pakistan:
    def language(self):
        print("Urdu")
        
class Punjab(Pakistan):
    def language(self):
        print("Punjabi")
        
class KPK(Pakistan):
    def language(self):
        print("Pasto")
        
pakistan = Pakistan()
pakistan.language()

punjab = Punjab()
punjab.language()

kpk = KPK()
kpk.language()


# In[12]:


#Polymorphism
# super() method
class Pakistan:
    def language(self):
        print("Urdu")
        
class Punjab(Pakistan):
    def language(self):
        super().language()
        
class KPK(Pakistan):
    def language(self):
        print("Pasto")
        
pakistan = Pakistan()
pakistan.language()

punjab = Punjab()
punjab.language()

kpk = KPK()
kpk.language()


# In[17]:


#Overloading
class Account:
    def createAcc(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def createAcc(self, name, email, password, mobileno):
        self.name = name
        self.email = email
        self.password = password
        self.mobileno = mobileno
        
    def showData(self):
        print(self.name)
        print(self.email)
        print(self.password)
        print(self.mobileno)
        
        
acc = Account()
acc.createAcc("john","john@gmail.com","password",123)
acc.showData()
        


# In[25]:


#Overloading
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def __add__(self, other):
        return( self.num1 + other.num1, self.num2 + other.num2)
    
    def __sub__(self, other):
        return( self.num1 - other.num1, self.num2 - other.num2)
    
    def __mod__(self, other):
        return( self.num1 % other.num1, self.num2 % other.num2)
        
s1 = Calculator(2, 4)
s2 = Calculator(3, 5)

s3 = s1 + s2
s4 = s1 - s2
s5 = s1 % s2
print(s3)
print(s4)
print(s5)


# In[30]:


#Abstract 
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def whatIEat(self):
        pass
    
class Lion(Animal):
    def whatIEat(self):
        print("Lion eats meat")
        
class Cow(Animal):
    def whatIEat(self):
        print("Cow eats grass")
        
class Dog(Animal):
    def whatIEat(self):
        print("Dog eats dog food and drink milk")
        
lion = Lion()
lion.whatIEat()

dog = Dog()
dog.whatIEat()

cow = Cow()
cow.whatIEat()


# In[ ]:




