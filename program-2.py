
salary = float(input("Enter your salary: "))
bonus = salary * 0.10
total = salary + bonus
tax = total * 0.05
final_salary = total - tax

print("Original Salary:", salary)
print("Bonus Added:", total)
print("After Tax Deduction:", final_salary)

