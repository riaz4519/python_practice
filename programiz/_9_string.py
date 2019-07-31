#create a string

my_string = "Hello"
print(my_string)

#with single quote

my_string = 'hello'

print(my_string)

#multililnes

my_string = """hello world 
dsfsfsd
"""

print(my_string)

#How to access characters in a string?
str = 'programiz'
print(str)

#first character
print(str[0])

#last character

print(str[-1])

#slicing 2nd to 5th

print(str[1:5])

#6th to 2nd last character

print(str[5:-3])

#can not delete a specific index or change have to del the whole string

#concate two string

print(str + my_string)

#usign * to make multiple

print(str *3)

#count number o l in stinf

count = 0
for latter in 'hello world':

    if latter == 'l':
        count += 1
print(count,'Latter found')

#list membership

print('a' in str)

print('f' not in str)

#len of string

len('hello world')

print(list(enumerate('Hello World')))

#format

print("{2}, is my first name {1} is last and {0} is middle".format('Fahim','riaz','md'))

#upper and lower method find 