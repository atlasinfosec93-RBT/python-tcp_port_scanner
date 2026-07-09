def banner():
    print("=== calculator ===")
    print("[made by @de4ault.93]")

banner()
#user input for operators and numbers
operator = input("Choose an operator (+, -, *, /): ")
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))

#if statments to perform the operaation based on the chosen operator

if operator == "+":
    result = input1 + input2
    print(f"result: {result}")
elif operator == "-":
    result = input1 - input2
    print(f"result: {result}")
elif operator == "*":
    result = input1 * input2
    print(f"result: {result}")
elif operator == "/":
    result = input1 / input2
    print(f"result: {result}")
else:
    print("Invalid operator")

def banner():
    print("[made by @de4ault.93]")