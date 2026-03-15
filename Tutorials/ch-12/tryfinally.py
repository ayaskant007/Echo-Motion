def main():
    try:
        a = int(input("Hey enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    print("I am inside finally.")

main()
