def safe_divide(numerator, denominator):
    # numerator = int(numerator)
    # denominator = (denominator)


    try:
        result = [float(numerator) / float(denominator)]
        print("The result of the division is", result)
    except (ZeroDivisionError, ValueError) as e:
        match e:
            case ZeroDivisionError():
                print("Error: Cannot divide by zero.")
            case ValueError():
                print("Error: Please enter numeric values only.")   

    # else:
    #     try:
    #         [float(numerator) / float(denominator)]

    #     except ValueError:
    #         print("Error: Please enter numeric values only.")   


    
    # else:
    #     print("Invalid Operation")