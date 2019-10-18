#normal

dict1 = {1:'Geeks',2:'for',3:'geeks'}

print(type(dict1))

#with different type

dict2 = {1:"geek",'name':"Fahim",'rol':5,'List':[1,2,3,5,6]}

#printing a dictonary
for x in dict2:
    print(dict2[x])

#creating with dict method

dict3 = dict({1:2,2:"faghi"})

#creating pair

dict4 = dict([(1,3),("FAhim",4)])

print(dict4)

#accessing

print(dict2[1])

print(dict2.get(1))

#removeing element

del dict2[1]

print(dict2)

print(dict2.pop('name'))