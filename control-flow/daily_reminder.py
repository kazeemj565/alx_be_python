task_description = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
task_due_date = input("Is it time-bound? (yes/no): ")
match task_priority:
    case "high":
        if task_due_date == "yes":
            print(f"Reminder: {task_description} is a {task_priority} priority task that requires immediate attention today!")
    case "low":
        if task_due_date == "no":
            print(f"Note: {task_description} is a {task_priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalide priority level. Please enter high, medium, or low as the priority.")