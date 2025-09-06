x = float(int("Please enter a temperature reading: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == "C":
    converted_temp = (x * 9/5) + 32
    print(f"{x}°C is {converted_temp}°F")
elif unit == "F":
    converted_temp = (x - 32) * 5/9
    print(f"{x}°F is {converted_temp}°C")