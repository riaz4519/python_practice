#variable

a = 3
b = 4
c = a + b
print(c)

d = a * b

print(d)

#conditional

if b % a == 0:
    print('is divisiable')
elif b > a:
    print ('B is greater then 3')

else:
    print('nothing')

#function

def checkWhoIsBig(a,b):

    if a > b :
        print("A is greater then b")
    else:
        print("B is greater then a")

checkWhoIsBig(a,b)