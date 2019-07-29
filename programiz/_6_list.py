#list

#create list
myList = [5,6,7,8]
print(myList)
#mixed data type list
myList = [5,8,'data',3.5]

print(myList)

#nested list

myList = ['hello',[5,6]]

print(myList)

#accessing the list

myList = ['p','r','o','b','e']

#by index
print(myList[0])

#nested
n_list = ["Happy", [2,0,1,5]]

print(n_list[1][1])

print(n_list[1])

#negative

print(myList[-1])

#slice list in python

listSlice = ['p','r','o','g','r','a','m','i','z']

#index 0 upto  index 3
print(listSlice[1:3])

#now begaining to last

print(listSlice[:])

#a certain number to last

print(listSlice[1:])

#change list or add list
odd = [2, 4, 6, 8]

#change the 1st item

odd[0] =1

print(odd)

odd[1:4] = [3,4,5]

print(odd)

#append list

odd.append(7)

print(odd)

#len

print(len(odd))

#extend

odd.extend([9,10,11])
print(odd)

#using + operator to extend

odd = odd + [1,5,6]
print(odd)

#repeat number

print(odd * 3)

#insert

odd.insert(1,10)