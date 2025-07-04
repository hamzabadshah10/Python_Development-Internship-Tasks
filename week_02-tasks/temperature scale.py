# Temperature Converter

try:

    Celsius = float(input("Enter temperature in Celsius: "))
    Fahrenheit = (Celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit = {Fahrenheit:.2f}°F")

except ValueError:
    print("Invalid input! Please enter a numeric value for Celsius.")

try:
    FahrenheitInput = float(input("\nEnter temperature in Fahrenheit: "))
    CelsiusConverted = (FahrenheitInput - 32) * 5/9
    print(f"Temperature in Celsius = {CelsiusConverted:.2f}°C")

except ValueError:
    print("Invalid input! Please enter a numeric value for Fahrenheit.")
