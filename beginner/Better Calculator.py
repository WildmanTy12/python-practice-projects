num1 = input("Enter a number: ")
op = input("Enter operator (+, -, *, /): ")
num2 = input("Enter another number: ")

if op == "+":
    result = float(num1) + float(num2)

elif op == "-":
    result = float(num1) - float(num2)

elif op == "/":
    result = float(num1) / float(num2)

elif op == "*":
    result = float(num1) * float(num2)

else:
    result = "Invalid operator!"

print("Result: ", result)
