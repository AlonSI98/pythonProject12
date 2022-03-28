Name = input("Enter name: ")
Age = int(input("Enter Age: "))
Date = int(input("Current year: "))
Nextdate = int(input("Choose your future year: "))
result = Nextdate - Date
megaresult = result + Age
print(f"{Name} wiil be {megaresult} years old in year {Nextdate}")