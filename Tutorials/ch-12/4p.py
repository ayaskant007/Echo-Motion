a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    print(f"The quotient of the divisiom is {a/b}")

except ZeroDivisionError:
    print("Infinite.")