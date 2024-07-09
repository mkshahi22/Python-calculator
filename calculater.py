# Welcome
print("Hello, Welcome to My Library")

# Collect 2 Numbers
num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))

while True:
    # Menu option
    print("\nChoose Number From 1 to 4:")
    print("Addition: 1")
    print("Subtraction: 2")
    print("Multiplication: 3")
    print("Division: 4")

    # User Choice Option
    num3 = int(input("\nEnter the Number: "))

    # Handling User Choice
    if num3 == 1:
        sum = num1 + num2
        print("Addition of {0} and {1} is {2}".format(num1, num2, sum))

    elif num3 == 2:
        sub = num1 - num2
        print("Subtraction of {0} and {1} is {2}".format(num1, num2, sub))

    elif num3 == 3:
        multi = num1 * num2
        print("Multiplication of {0} and {1} is {2}".format(num1, num2, multi))

    elif num3 == 4:
        if num2 != 0:
            div = num1 / num2
            print("Division of {0} and {1} is {2}".format(num1, num2, div))
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid Number")

    # Ask user if they want to continue
    cont = input(
        "Do you want to perform another operation? (yes/no): ").strip().lower()
    if cont != 'yes':
        break
