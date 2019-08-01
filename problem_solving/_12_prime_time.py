number = int(input())

prime = True
#check for prime number
for i in range(2,number//2):
    if number % i == 0:
        prime = False
        break

print(prime)