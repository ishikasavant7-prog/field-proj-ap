# Get a number from the user
num = int(input("Enter a positive number: "))

factorial = 1
# Check if the number is positive
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
