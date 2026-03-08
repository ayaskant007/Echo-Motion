num = int(input("Enter a number which you want to check: "))

if num <= 1:
    print("This number is neither prime nor composite")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("This number is prime")
    else:
        print("This number is composite")
    