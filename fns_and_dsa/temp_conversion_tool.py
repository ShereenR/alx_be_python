FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5
def convert_to_celsius(fahrenheit):
    celsius = (choice_temp - 32) * 5 / 9
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
choice_temp=float(input("Enter the temperature to convert:"))
choice_temp2=input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if choice_temp2=="c":
    converted_temp=convert_to_fahrenheit(choice_temp)
    print(f"{choice_temp} °F is {converted_temp:.2f} °C")
elif choice_temp2 =="f":
    converted_temp=convert_to_celsius(choice_temp)
    print(f"{choice_temp} °F is {converted_temp:.2f} °C")
else:
    print("Invalid temperature. Please enter a numeric value")