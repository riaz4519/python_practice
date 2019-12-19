string1 = "This is a test string for test"
print(string1)

#as it is

string_as_it_is = '''Th is is a as 
                    as its is '''

print(string_as_it_is)

#accessing characters

#first character
print(string1[0])
print(string1[-len(string1)])
#last character
print(string1[-1])
print(string1[len(string1)-1])

#string slicing

#pring 3rd ti 12th
print(string1[3:12])