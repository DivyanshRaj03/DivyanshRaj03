from temperature.celsius_to_fahrenheit import celsius_to_fahrenheit
from temperature.fahrenheit_to_celsius import fahrenheit_to_celsius
from temperature.celsius_to_kelvin import celsius_to_kelvin

def main():
    print("Temperature Conversion Option:")
    print("1. Celsius to Fahrenhite")
    print("2. Fahrenhite to Culsius")
    print("3. Celsius to Kelvin")
    
    choice = int(input("Enter your choise (1/2/3):"))
    
    if choice == 1:
        Celsius = float(input("Enter temperature in Celsius: "))
        print(f"{Celsius}°C = {celsius_to_fahrenheit(Celsius)}°F")
         
    elif choice == 2:
        Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{Fahrenheit}°F = {fahrenheit_to_celsius(Fahrenheit)}C")
        
    elif choice == 3:
        Celsius = float(input("Enter temperature in Celsius"))
        print(f"{Celsius}°C = {celsius_to_kelvin(Celsius)}°K")
        
    else:
        print("Invalid choice")
        
main()