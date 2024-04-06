"""
ChatBot
Ali Altaf
Date: March 8, 2024
Description: Python file that takes temperature, integers, and products from the user
"""
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


if __name__ == "__main__":
    name = input("Enter your name: ")
    print("What's up,", name)

    x = 10
    y = 5
    z = x * y
    print("The product of", x, "and", y, "is", z)

    number = float(input("Enter a number: "))
    check_number(number)

    strVar = input("Enter your integer number:")
    intVar = int(strVar)
    floatVar = float(strVar)
    print("The string:", strVar, "The integer:", intVar, "The float:", floatVar)

    celsius_temp = float(input("Enter temperature in Celsius: "))
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print("In freedom (fahrenheit) units, this is:", fahrenheit_temp)
    print("Nice talking with you, bye")
