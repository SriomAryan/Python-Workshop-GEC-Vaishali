Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Day 7

#Dictionary
D={}
type(D)
<class 'dict'>
D={101:"CE",102:"ME",105:"CSE"}
D
{101: 'CE', 102: 'ME', 105: 'CSE'}
D.keys()
dict_keys([101, 102, 105])
D.values()
dict_values(['CE', 'ME', 'CSE'])
D[105]
'CSE'
D[105]="CSE(IOT)"   #Updating
D
{101: 'CE', 102: 'ME', 105: 'CSE(IOT)'}
D.pop(105)
'CSE(IOT)'
D
{101: 'CE', 102: 'ME'}
D.items()
dict_items([(101, 'CE'), (102, 'ME')])
D.update({105:["CSE","CSE(IOT)"]})
D
{101: 'CE', 102: 'ME', 105: ['CSE', 'CSE(IOT)']}
D[105][1]
'CSE(IOT)'
D[105][0]
'CSE'


#OOPs (Object Oriented Programming)
#OOPs concepts:- Object,Class,Encapsulation,Inheritance,Polymorphism,Abstraction

#Class
class car:
    def_init_(self):
        
SyntaxError: invalid syntax
class car:
    def _init_(self):
        self.brand="BMW"
        self.colour="Black"
        self.top_speed=250

        
Car=car()
Car.brand
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Car.brand
AttributeError: 'car' object has no attribute 'brand'
car.brand
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    car.brand
AttributeError: type object 'car' has no attribute 'brand'
Car.brand
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    Car.brand
AttributeError: 'car' object has no attribute 'brand'



KeyboardInterrupt
class car:
    def __init__(self):
        self.brand="BMW"
        self.colour="Black"
        self.top_speed=250

        
Car=car()
Car.brand
'BMW'
Car.colour
'Black'
AttributeError: 'car' object has no attribute 'brand'
SyntaxError: invalid syntax

class Car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.colour=c
        self.top_speed=ts

        
car=Car("Ferrari","Red",280)
car.brand
'Ferrari'
car.colour
'Red'
car.top_speed
280

class Car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.colour=c
        self.top_speed=ts
...     def acceleration():
...         print("Your car top speed is:",self.top_speed)
... 
...         
>>> car=Car("Ferrari","Red",280)
>>> 
>>> 
>>> class Car:
...     def __init__(self,b,c,ts):
...         self.brand=b
...         self.colour=c
...         self.top_speed=ts
...     def acceleration():
...         print("Your car top speed is:",self.top_speed)
... 
...         
>>> class Car:
...     def __init__(self,b,c,ts):
...         self.brand=b
...         self.colour=c
...         self.top_speed=ts
...     def acceleration(self):
...         print("Your car top speed is:",self.top_speed)
... 
...         
>>> car=Car("Ferrari","Red",280)
>>> car.acceleration()
Your car top speed is: 280
>>> 
>>> 
>>> class student:
...     def __init__(self,a,b,c,d):
...         self.name=a
...         self.branch=b
...         self.roll_number=c
...         self.cgpa=d
... 
...         
>>> Person=student("Sriom","CSE(IOT)",9,8.2)
>>> Person.name
'Sriom'
>>> Person.branch
'CSE(IOT)'
>>> Person.roll_number
9
>>> Person.cgpa
8.2
>>> 
>>> 
