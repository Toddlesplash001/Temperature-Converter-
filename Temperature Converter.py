a = float(input("Enter the temperature "))
b = input("Enter type of temperature ")
if b.upper() == "CELSIUS":
    fahrenheit = 1.8*a + 32
    print("The temperature in fahrenheit is", fahrenheit,"F")
    kelvin = a + 273.15
    print("The temperature in kelvin is", kelvin,"K")
if b.upper() == "FAHRENHEIT":
    celsius = 5/9*(a-32)
    celsius = int(celsius)
    print("The temperature in celsius is", celsius,"C")
    kelvin = celsius+273.15
    print("The temperature in kelvin is", kelvin,"K")
if b.upper() == "KELVIN":
    celsius = a - 273.15
    print("The temperature in celsius is", celsius,"C")
    fahrenheit = 1.8*a + 32
    print("The temperature in fahrenheit is", fahrenheit,"F")


        
