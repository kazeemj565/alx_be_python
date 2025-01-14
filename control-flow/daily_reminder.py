description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
due_date = input("Is it time-bound? (yes/no): ")
match (priority):
    case "high":
        if due_date == "yes":
            print(f"Reminder: {description} is a {priority} priority task that requires immediate attention today!")
    case "low":
        if due_date == "no":
            print(f"Note: {description} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalide priority level. Please enter high, medium, or low as the priority.")