

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]

print(table)


with open("Tables.txt", "w") as f:
    data = f.write(str((table)) + "\n")