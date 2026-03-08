a = []

elements = int(input("Enter no. of elements:"))

for i in range(elements):
    b = int(input("Enter no.: "))
    a.append(b)

a.sort()

print(f"{a[elements-1]} is the greatest number")