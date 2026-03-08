import time

a = int(input("Enter your age:  "))

if a > 18:
    print("You're an adult.")

elif a < 0:
    print("Invalid Age")

elif a == 0:
    print("Invalid Age age 0  is not possible.")

else:
    time.sleep(3)
    exit("You're not an adult..")
