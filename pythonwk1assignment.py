#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).

num1 = int (input("Enter a value for x"))
num2 = int (input("Enter a value for y"))
sign = input("Enter the operation, +, -, /, *")

if sign == "+":
    result = num1 + num2
elif sign == "-":
    result = num1 - num2   
elif sign == "*":
    result = num1 * num2   
elif sign == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error cant divide with 0 Dummie" 
else:
    result = "Invalid operator!"  

print(str(num1) + " " + str(sign) + " " + str(num2) + " = " + str(result))