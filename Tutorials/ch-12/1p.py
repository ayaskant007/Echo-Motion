try:
    with (
        open("1.txt", "r") as f,
        open("2.txt", "r") as f1,
        open("3.txt", "r") as f2
    ):
            data1 = f.read()
            data2 = f1.read()
            data3 = f2.read()
    
except FileNotFoundError:
    print("Files are not present.")