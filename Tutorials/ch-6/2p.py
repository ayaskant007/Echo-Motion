subjects = int(input("Enter number of elements:"))
total=100
perctotal = 100*subjects
for i in range(subjects):
    a = int(input("Enter marks: "))
    sum = a + 0
    if a<33%total:
        print("You Have Failed this subject and this grade.")
        exit()
    else:
        print("You have passed this subject.")
    
if sum<40%perctotal:
    print("You have failed to secure the minimum 40% total marks to pass.")
else:
 print("You have acquired the total 40\\% of marks to pass.")