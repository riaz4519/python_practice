#create array

import array

arr = array.array('i',[1,2,3])

print(arr[1])

#add new array

arr.append(2)

print(arr)

#add with position

arr.insert(2,5)

print(arr)

#remove with pop

arr.pop()
arr.pop(1)

#remove with remove

arr.remove(5)

print(arr.index(1))

print(arr.reverse())