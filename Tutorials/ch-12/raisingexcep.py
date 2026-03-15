

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if (b==0):
    raise ZeroDivisionError("Hey our program is not designed to divide by 0.")

print(f"The division of the numbers is {a/b}")