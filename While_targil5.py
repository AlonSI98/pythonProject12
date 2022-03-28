num1= int(input("enter your 2 digits number here: "))
num2= 7
while 10<=num1<=99:
    if num1%num2==0 or num1%10==7 or num1//10%10==7:
        print("You got lucky number")
        num1 = int(input("enter your 2 digits number here: "))
    else:
        print("Try again")
        num1 = int(input("enter your 2 digits number here: "))