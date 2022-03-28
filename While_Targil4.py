num1 = int(input("enter your number here: "))
num2 = int(input("enter another number here: "))
num3= 10
num4= 1
while num1<=10 and num2<=10:
    if num1+num2==num3:
        print(10)
        num1 = int(input("enter your number here: "))
        num2 = int(input("enter another number here: "))
        if num1+num2>10 or num1+num2<10:
            print("goodbye")