monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expenses
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print("Your monthly savings are: $%s" % monthly_savings)
print("Projected savings after one year, with interest, is: $%s" % projected_savings)

