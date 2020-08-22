# Script to convert Fahrenheit to Celcius
fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius?: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} fahrenheit is {celsius:.1f} celsius.")
