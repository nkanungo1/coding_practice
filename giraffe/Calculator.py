#normal addition
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)
#int used for whole numbers whereas float used for whole as well as decimals

num1 = float(input("Enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 /num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")