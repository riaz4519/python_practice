#making  4 function

def addition(num1,num2):

    return  num1 + num2

#sub

def subtract(num1,num2):

    return  num1 - num2

def multiply(num1,num2):

    return  num1 * num2

def division(num1,num2):

    return  num1/num2

#printing what to do

print("Please select operation -\n"\
      
      "1.Add\n"\
      "2.Subtract\n"\
      "3.Multiply\n"\
      "4.Division"
      )
select = int(input("select one of the option : "))

num1 = int(input("insert number 1:"))
num2 = int(input("insert number 2:"))

#decision making

if select == 1:
    print("sum of ",num1,"and",num2,"is",addition(num1,num2))
elif select == 2:
    print("sub of ",num1,"and",num2,"is",subtract(num1,num2))
elif select == 3:
    print("multi of ",num1,"and",num2,"is",addition(num1,num2))
elif select == 4:
    print("Division of ",num1,"and",num2,"is",addition(num1,num2))
else:
    print("invalid input")