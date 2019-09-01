
#1st dimension

print([i for i in range(10)])

#even number

print(list(range(0,10,2)))

print([i for i in range(10) if i % 2 == 0])

#with multi loop

#sum

print([i+j for i in range(10) for j in range(i+1)])

#list in list

print([[i,j] for i in range(10) for j in range(i+1)])