print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")
options = int(input("Select the operation (1/2/3/4): "))
result = 0
if (options in [1, 2, 3, 4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if (options == 1):
        result = num1 + num2

    elif options == 2:
        result = num1 - num2
        
    elif options == 3:
        result = num1 * num2
    elif options == 4:
        result = num1 / num2
else:
     print("Invalid Operation Entered. Please try again.")

print("The result of the operation is: ", result)