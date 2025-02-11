"""Hoy crearemos un programa de nivel principiante dedicado a nuestros amigos indios.
India es el hogar de numerosos festivales que se celebran durante todo el año, por lo
que en este proyecto, creará un programa simple que recuerde a los usuarios los próximos
festivales indios. El programa tomará la fecha de hoy como entrada, la comparará con un 
diccionario predefinido de fechas de festivales y notificará al usuario
si se acerca un festival."""

import datetime

# Diccionario con las fechas de festivales de India (formato MM-DD)
festivals = {
    "Diwali": "11-01",
    "Holi": "03-25",
    "Navratri": "10-03",
    "Raksha Bandhan": "08-19",
    "Eid": "04-10",
    "Pongal": "01-14",
}

today = datetime.date.today()   
current_year = today.year
upcoming_festival =  None
min_days  =float("inf")
# Recorremos el diccionario y compara la fecha de hoy con las fechas de festivales

for festival, date in festivals.items():
    month, days = map(int, date.split("-"))

    # Crear fecha con el año actual
    festival_date = datetime.date(current_year, month, days)

# Si la fecha ya pasó este año, ajustar al próximo año
    if festival_date < today:
        festival_date = datetime.date(current_year + 1, month, days)

 # Calcular los días faltantes
    delta_days = (today - festival_date).days
 
    if delta_days < min_days:
        min_days = delta_days
        upcoming_festival = (festival, min_days)

# Imprimir solo el festival más cercano
if upcoming_festival:
    festival_name, days_left = upcoming_festival
    print(f"The next festival is: {festival_name} and is missing: {days_left} days.")

