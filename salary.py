basic_pay = float(input("Enter basic pay: "))
hra = 0.10 * basic_pay
ta = 0.05 * basic_pay
salary = basic_pay + hra + ta
print("Total Salary =", salary)
