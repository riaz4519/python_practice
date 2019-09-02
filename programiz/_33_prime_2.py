
def in_prime(x):

    for i in range(2,x//2):

        if x % i == 0 :

            return  False
    else:
        return  True

print(in_prime(5))