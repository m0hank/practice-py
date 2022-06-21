# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

def displayWelcome ():
    
    print("This program will convert a range of temperatures")
    print("Enter (F) to convert Fahrenheit to Celsius")
    print("Enter (C) to convert Celsius to Fahrenheit")

def getCovertTo():

    which = input("Enter Selection: ")
    while which != 'F' and which != 'C':
        which = input("Enter Selection: ")
    return which

def displayFahrentoCelsius(start, end):

    print('\n Degrees', 'Degress')
    print('Fahrenheit', 'Celsius')

    for temp in range(start, end + 1):
        converted_temp = (temp - 32) * 5/9
        print(' ' .format(temp, '4.lf'), '  ' .format(converted_temp, '4.lf'))

def displayCelsiustoFahern(start, end):

    print('\n Degress', 'Degress')
    print('  Celsuis', 'Fahrenheit')

    for temp in range(start, end + 1):
        converted_temp = (9/5 * temp) + 32
        print(' ' .format(temp, '4.lf'), ' ' .format(converted_temp, '4.lf'))

# ---- main

# Display program welcome
displayWelcome()

# Get which conversion from user
which = getCovertTo()

# Get range of temperatures to convert
temp_start = int(input("Enter starting temperature to convert: "))
temp_end = int(input("Enter ending temperature to convert: "))

# Display range of converted temperatures
if which == 'F':
    displayFahrentoCelsius(temp_start, temp_end)
else:
    displayCelsiustoFahern(temp_start, temp_end)
