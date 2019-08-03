numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
    sum += val
print("The sum is ",sum)

#the range function

print(range(10))

#range with list

print(list(range(10)))

#range with step

print(list(range(0,10,3)))

#with the help of list len
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print('I like ',genre[i])