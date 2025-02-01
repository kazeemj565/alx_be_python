def safe_divide(numerator, denominator):
    numerator = int(numerator)
    denominator = int(denominator)


    try:
        # if denominator != 0:
        result = float(numerator / denominator)
        print("The result of the division is", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Please enter numeric values only.")   


    
    # else:
    #     print("Invalid Operation")