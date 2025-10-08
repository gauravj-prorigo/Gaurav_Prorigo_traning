
print(" Welcome to the Basic Arithmetic Calculator")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (**)")
print("4. Division (/)\n")


choice = input("Enter the operation (1/2/3/4 or + - * /): ")


if choice in ('1', '+'):
    result = num1 + num2
    operator = '+'
elif choice in ('2', '-'):
    result = num1 - num2
    operator = '-'
elif choice in ('3', '*'):
    result = num1 * num2
    operator = '*'
elif choice in ('4', '/'):
    if num2 == 0:
        print(" Error: Cannot divide by zero.")
        exit()
    result = num1 / num2
    operator = '/'
else:
    print(" Invalid operation selected.")
    exit()


print(f"\n✅ Result: {num1} {operator} {num2} = {result}")
