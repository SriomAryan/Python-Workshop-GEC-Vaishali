Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='Aryan'
type(s)
<class 'str'>
a="""Python workshop
Day 6, Topic strings"""
type(a)
<class 'str'>
s[0]
'A'
s[1]
'r'
s[2]
'y'
s[3]
'a'
s[4]
'n'
s[5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[5]
IndexError: string index out of range
s[-1]
'n'
s[-2]
'a'
s[-3]
'y'
s-4]
SyntaxError: unmatched ']'
s[-4]
'r'
s[-5]
'A'
s="Government Engineering Colllege Vaishali"
s[0:3]
'Gov'
s[-8:-1]
'Vaishal'
s[-9:-1]
' Vaishal'
s[-8:0]
''
s[1:15]
'overnment Engi'
len(s)
40
s[0:40]
'Government Engineering Colllege Vaishali'
s[0:20]
'Government Engineeri'
s[-40:-1]
'Government Engineering Colllege Vaishal'

a="Sriom "
b="Aryan "
c="Mallick "
a+b+c
'Sriom Aryan Mallick '

s="Sriom"
print("My Name is %s",%s)
SyntaxError: invalid syntax
print("My Name is %s"%s)
My Name is Sriom


L=["Sriom",9,True]
type(L)
<class 'list'>
l[0]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l[0]
NameError: name 'l' is not defined. Did you mean: 'L'?
L[0]
'Sriom'
L[1]
9
L[2]
True
L
['Sriom', 9, True]
L[1]=8.15
L[1]
8.15
L
['Sriom', 8.15, True]

KeyboardInterrupt
L=["Sriom",9,True]
L.append(9)
L
['Sriom', 9, True, 9]
L.insert(4,8.15)
L
['Sriom', 9, True, 9, 8.15]
L.pop()
8.15
L
['Sriom', 9, True, 9]
L.pop()
9
L
['Sriom', 9, True]
L.append(8.2)
L
['Sriom', 9, True, 8.2]
>>> L.remove(4)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    L.remove(4)
ValueError: list.remove(x): x not in list
>>> L.remove(8.2)
>>> L
['Sriom', 9, True]
>>> L[0:2]
['Sriom', 9]
>>> len(L)
3
>>> 
>>> #TUPLE
>>> t=("Aryan",8.15,14)
>>> type(t)
<class 'tuple'>
>>> t[0]
'Aryan'
>>> t[1]
8.15
>>> t[2]
14
>>> t[1]=9
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    t[1]=9
TypeError: 'tuple' object does not support item assignment
>>> 
>>> #tuple is immutable
\
>>> 
>>> 
>>> #SETS
>>> s={"Sriom","Aryan","Mallick"}
>>> type(s)
<class 'set'>
>>> a=set([1,2,3,4,5,6])
>>> type(a)
<class 'set'>
>>> a.add("9")
>>> A
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> a
{1, 2, 3, 4, 5, 6, '9'}
