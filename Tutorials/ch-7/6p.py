n = int(input("Enter the number till which u want a factorial of:"))
total = 1

for i in range(1, n+1):
    total = total * i

print(total)
