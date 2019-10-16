#creating a set

set1 = set('geeks')

print (set1)

#set from list

lis1 = [1,2,35,468,12,9,3,57,62,47,6,14,9,2,37]

new_list1 = set(lis1)

print(new_list1)

#adding to set

new_list1.add(25)

print(new_list1)

#update

new_list1.update([4,6,8,45])
print(new_list1)

#check if exits or not

print (6 in new_list1)

#remove

new_list1.remove(6)

print(new_list1)

#discard