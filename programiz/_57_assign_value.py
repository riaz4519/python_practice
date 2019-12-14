from operator import itemgetter
from itertools import compress
#normal
a = 5
#with condition
b = 1 if a > 7 else 0
#print(a,b)

#multiple value assigning
test_list = [1, 4, 5, 6, 7, 3]
var1 , var2 ,var3 = [test_list[i] for i in  (1,2,5)]

print(var3)

#using itemgetter

var1,var2,var3 = itemgetter(1,3,5)(test_list)

print(var2)

#using item tools compress

var1,var2,var3 = compress(test_list,(1,0,0,1,1,0))

print(var3)