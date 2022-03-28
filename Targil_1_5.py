salary=int(input("enter salary: "))
precent=int(input("enter raise precent: "))

salary_raise = salary*precent/100
new_salary=salary+salary_raise
print("The new salary is", new_salary)