print("Geeks: % 2d ,portal : % 5.2f"%(1,05.33))

#with format method

print('I love {} for {}'.format("Geeks","Geeks"))

#with position

print("I Love  {0} and {1}".format("Geeks",'Portal'))

#with position two

print("I love {1} and {0}".format("geeks","portal"))

#with position and arguments

print("I love {0},{1} and {other}".format("geeks","for",other="geeks"))

#using format with number

print("Geeks :{0:2d},Portal {1:8.2f}".format(12,00.546))

#changin position argument

print("Second argument :{1:3d},first argument:{0:7.2f}".format(47.42,11))

#keyword with format

print("{a:3d} {b:3.2f}".format(a=20,b=4.55))

#printing center

cstr = "I love geeksforgeeks"
print(cstr.center(40,'#'))

#printing left

print(cstr.ljust(40,"-"))





