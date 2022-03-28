num1 = int(input("Enter your fisrt number here: "))
num2 = int(input("Enter your second number here: "))
while num1%2==0 or num2%2==0:
    if num1%2==0 and num2%2==0:
        print(num1*num2)
        num1 = int(input("Enter your fisrt number here: "))
        num2 = int(input("Enter your second number here: "))
    else:
        print(num1+num2)
        num1 = int(input("Enter your fisrt number here: "))
        num2 = int(input("Enter your second number here: "))