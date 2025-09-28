def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x, y):
    if y == 0:
        print("Error! Cannot divide by 0.")
    return x / y

print("Choose an Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = ''

while choice not in ['1', '2', '3', '4']:
    choice = input("Enter a choice 1 - 4: ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Try again.")

num1 = float(input("Enter in a number: "))
num2 = float(input("Enter in a number: "))

if choice == '1':
    print("Results: ", add(num1, num2))
elif choice == '2':
    print("Results: ", subtract(num1, num2))
elif choice == '3':
    print("Results: ", multiply(num1, num2))
elif choice == '4':
    print("Results: ", divide(num1, num2))
else:
    print("Incorrect input! Try again.")
