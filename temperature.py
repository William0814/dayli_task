"""Al ejecutar el programa debería aparecer la lista original de temperaturas
en Fahrenheit y la lista de temperaturas en Celsius:"""


while True:
    user_temperature = float(input('Enter the temperature: '))
    temperature_type = input('F° or C°: ')
    match temperature_type:
        case 'F°':
            fahrenheit = (user_temperature-32)*5/9
            print(f'Temperature fahrenheit to celsius: {fahrenheit} F°')
            break
        
        case 'C°':
            celsius = (user_temperature+32)*5/9
            print(f'Temperature celsius to fahrenheit: {(celsius)} C°')
            break

        case anything:
            print('Command invalid please only F° or C°!!')



    
   















""""print(f'Temperature in Farerenheit: {temperatures_fahrenheit}')
print(f'Temperature in Celsius: {celsius}')"""
