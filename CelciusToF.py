def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Get the Celsius temperature from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius:.2f} C is {fahrenheit:.2f} F")
