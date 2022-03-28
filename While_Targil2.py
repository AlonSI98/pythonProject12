age = int(input("Enter your age here: "))
while 0<=age<=120:
    if 0<=age<=18:
        print("child")
        age = int(input("Enter your age here: "))
        if 19<=age<=60:
            print("adult")
            age = int(input("Enter your age here: "))
            if 61<=age<=120:
                print("senior")
                age = int(input("Enter your age here: "))