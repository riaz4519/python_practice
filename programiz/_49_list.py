List = [7,"data",7.2]

List_multi = [['data',4,5],['hello','hi',7]]

#access

print(List[0])
print(List)
#adding element

List.append(1)

print(List)
#insert
List.insert(0,1)

print(List)

#extend

List.extend([1,3,3,])

print(List)

#remove by value

List.remove(3)
print(List)

List.pop()

print(List)

List.pop(2)

print(List)