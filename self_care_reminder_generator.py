"""Escriba un programa que sugiera con delicadeza actividades de autocuidado para el día. 
El programa selecciona al azar una actividad de una lista predefinida de acciones relajantes
 y calmantes para promover el bienestar mental."""

import random
self_care_activities = [
    "Take a short walk in nature. 🌿",
    "Drink a big glass of water. 💧",
    "Do some deep breathing for 5 minutes. 🧘‍♂️",
    "Listen to your favorite music. 🎵",
    "Write down three things you're grateful for. ✨",
    "Read a chapter from a book you love. 📚",
    "Stretch your body gently. 🤸‍♀️",
    "Spend a few minutes with a pet or a loved one. 🐾",
    "Watch the sunset or sunrise. 🌅"
]

while True:
    user = input('Do you want execut the programm yes/no? ')
    user = user.strip()
    match user:
        case 'yes' | 'YES':
            activity = random.choice(self_care_activities)
            print(f' Hello! Here is your self-care suggestion for today: {activity}')
            break
        
        case 'no' | 'NO':
            print('Ok, see you tomorrow !!')
            break

        case anything:
            print('Command invalid, please enter yes or no.')
            print('-----Try again.-----')
    