FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
degree_sign = u"\u00B0"

def convert_to_celsius(fahrenheit):
    temp_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_celsius


def convert_to_fahrenheit(celsius):
    temp_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp_fahrenheit
    


temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrrenheit? (C/F): ")
if unit == "F":
    new_temp = convert_to_celsius(temperature)
    print(f"{temperature}{degree_sign}F is {new_temp} C")

elif unit == "C":
    new_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}{degree_sign}C is {new_temp} F")

else:
    print("Invalid unit. Please enter C or F.")
