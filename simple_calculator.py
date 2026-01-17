a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
ch = input("Choose operator (+, -, *, %, /): ")

if ch == '+':
    print("Result:", a + b)

elif ch == '-':
    print("Result:", a - b)

elif ch == '*':
    print("Result:", a * b)

elif ch == '%':
    print("Result:", a % b)

elif ch == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator selected")