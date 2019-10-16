#creating a touple

touple1 = ()

print(type(touple1))

touple1 = (1,2,5,"hello")

print(touple1)

#touple from list
List1 = [1,3,5,6,9,4]

touple1 = tuple(List1)

print(touple1)

#tuple with function

tuple3 = "Geeks"

new_tuple3 = tuple(tuple3)

print(new_tuple3)

#concate tuple

concate_tuple = touple1 + new_tuple3;

print (concate_tuple)