import keyword
import ast

print(keyword.kwlist)

print(keyword.iskeyword('for'))

#if condition

i = 10
b = 15
if (i > b):
    print(i,'is less  then',b,end="")
else:
    print('data')

#if else elif

value = input().strip()
if value.isdigit():
    print(type(value))
elif value.isalpha():
    print(type(value))
elif value.isdecimal():
    print(value)
else:
    print('No type')