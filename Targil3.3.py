num1 = (input("Enter the number of computers you worked on today: "))
if num1=="":
    num1=15
    print("The number of computers you need to work on tomorrow is: " , num1*2)
else:
    num1=int(num1)
    print("The number of computers you need to work on tomorrow is: " , num1*2)


