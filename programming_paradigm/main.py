import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()


# import sys
# from robust_division_calculator import safe_divide

# def main():
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <numerator> <denominator>")
#         sys.exit(1)

#     numerator = sys.argv[1]
#     denominator = sys.argv[2]

#     safe_divide(numerator, denominator)

# if __name__ == "__main__":
#     main()


     # try:
    #     result = [float(numerator) / float(denominator)]
    #     print("The result of the division is", result)
        
    # except (ZeroDivisionError, ValueError) as error:
    #     match error:
    #         case ZeroDivisionError():
    #             print("Error: Cannot divide by zero.")

    #         case ValueError():
    #             print("Error: Please enter numeric values only.")

