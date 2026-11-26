# these are the arthmatics function 

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def division(a, b):
    return a / b

# this is the main function which we are calling

def main_cal(num1, num2, op):
    operation = ["+", "-", "*", "/"]
    if op == operation[0]:
        return add(num1, num2)
    elif op == operation[1]:
        return subtract(num1, num2)
    elif op == operation[2]:
        return multiply(num1, num2)
    elif op == operation[3]:
        if num2 == 0:
            return "infinite value"
        else:
            return division(num1, num2)
    else:
        return "invalid opration"

# this is where i called the function where i used 
#while loop and inside i user if/else condition 
while True :
    asked = input("enter do yo want to calculate: ").lower()
    if asked == "yes":
        print("ok")
    else:
        break
    a = float(input("enter the number: "))
    b = float(input("enter the number: "))
    oper = input("enter the operation: ")
    print(main_cal(a, b , oper))


        
