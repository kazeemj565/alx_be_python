monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = float(monthly_income - total_monthly_expenses)
# monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print("Your monthly savings are: $%s" % monthly_savings)
print("Projected savings after one year, with interest, is: $%s" % projected_savings)

