dict2= {}

friends = int(input("Enter no of friends: "))
for i in range(friends):
    name = input("Enter your name: ")
    subject = input("Enter your favorite subject: ")
    dict2.update({name: subject})
    print(f"{name}'s favorite subject is {dict2.get(name)}")

print(dict2)
    