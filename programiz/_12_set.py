#declear

my_set = {1,2,3}

#set of mixed types
my_set = {1.0,"hello",(1,2,3)}

my_set = {1,3}

#adding to a set
my_set.add(2)

print(my_set)

#add multiple element

my_set.update([2,34,56])
print(my_set)

#adding list and set

my_set.update([85,65,45],{45,98,36})

#remove from set

my_set_remove = {1, 3, 4, 5, 6}
print(my_set_remove)

my_set_remove.discard(4)

print(my_set_remove)

#pop is here to

my_set_remove.pop()
print(my_set_remove)