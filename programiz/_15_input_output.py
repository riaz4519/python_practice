#noraml print

print('This is a normal print')

#print with a variable
a = 5
print("The value of a is",a)

#print with sep and end

print(1,2,3,4,sep='#',end='&')

#output formating str.format()

first_name ,last_name = 'Fahim','Riaz'

print('My first Name is {} last Name is{}'.format(first_name,last_name))

#output formatting with index

print('My firstname is {0} and last name is {1}'.format('Fahim','Riaz'))
print('My firstname is {1} and last name is {0}'.format('Fahim','Riaz'))

#output formattion with arguments

print("this is my {first_name} this is my last_name {last_name}".format(first_name='Fahim',last_name='Riaz'))

#output formatiing like c programming
x  = 111.2
print('the value %.4f' %x)
