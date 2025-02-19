"""Project Description
Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin using functions.

How the Program Works
When executed, the program asks the user to enter a value. For example,
in the demo below, the user is entering 10:"""

import functions

while True:
    print('Temperature Converter \n'
        '================================')
    
    user_temperature = input('Enter your temperature: ')
    try:
        user_temperature = float(user_temperature)
    except ValueError:
        print('Invalid input, please enter a number.')
        continue

    print('Choose the conversion: \n'
        '1. Celsius to Fahrenheit \n'
        '2. Fahrenheit to Celsius \n'
        '3. Kelvin to Celsius \n'
        '4. Celsius to Kelvin \n')

    user_select = int(input('Enter your choice (1-4): '))

    if user_select == 1:
        fahrenheit = functions.celsius_to_fahrenheit(user_temperature)
        print(f'{user_temperature} Celsius is equal to {fahrenheit:.3f} Fahrenheit.')
        break

    elif user_select == 2:
        celsius = functions.fahrenheit_to_celsius(user_temperature)
        print (f'{user_temperature} Fahrenheit is equal to {celsius:.3f} Celsius.')
        break

    elif user_select == 3:
        celsius = functions.kelvin_to_celsius(user_temperature)
        print(f'{user_temperature} Kelvin is equal to {celsius:.3f} Celsius.')
        break

    elif user_select == 4:
        kelvin = functions.celsius_to_kelvin(user_temperature)
        print(f'{user_temperature} Kelvin is equal to {kelvin:.3f} Celsius.')
        break

    else:
        print(f'{user_select} is not valid command, please try again.')
        continue
    


 