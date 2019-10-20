
#unpacking
def my_sum(a,b,c):
    print(a,b,c)


list1 = [1,2,3]

my_sum(*list1)

#packing

def packing_sum(*args):

    sum = 0
    for sinlge in args:

        sum = sum + sinlge

    return  sum

print (packing_sum(1,2,3,4,5,6,7,8))

#there is for dictionary