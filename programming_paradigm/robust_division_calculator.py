def safe_divide(numerator, denominator):
    # try:
    #     result = [float(numerator) / float(denominator)]
    #     print("The result of the division is", result)
        
    # except (ZeroDivisionError, ValueError) as error:
    #     match error:
    #         case ZeroDivisionError():
    #             print("Error: Cannot divide by zero.")

    #         case ValueError():
    #             print("Error: Please enter numeric values only.")


    try:
        result = float(numerator) / float(denominator)
        print("The result of the division is", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")



# safe_divide(4, 3)
# safe_divide(4, 0)
# safe_divide(4, 'jan')
