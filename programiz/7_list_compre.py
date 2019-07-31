comList = [x for x in range(10)]
print(comList)

#with condition
conditionList = [x for x in range(0,20) if x % 2 == 0]
print(conditionList)

#more then one loop

twoLoop = [x+y for x in range(10) for y in range(10)]

print('list is :',twoLoop,'Length is :',len(twoLoop))
