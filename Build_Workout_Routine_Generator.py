"""Create a program that suggests random workout routines based on user input, 
making fitness more engaging and personalized."""

import random

strenght = ["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
cardio = ["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
flexibility = ["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

print('Welcome to the workout Routine Generator!')
print('Choose your workout type: \n'
          '1. Strength Training \n'
          '2. Cardio \n'
          '3. Flexibility \n')
print('-------------------------------------------')
while True:
    user_choice = input("Enter your choice of 1-3 only numbers:")

    try:
        user_choice = int(user_choice)
    except ValueError:
        print('Invalid input, please enter a number between 1 and 3.')
        print('-------------------------------------------')
        continue

    
    

    match user_choice:
        case 1:
            print(f'Try this exercise: {random.choice(strenght)}')
            break

        case 2:
            print(f'Try this exercise: {random.choice(cardio)}')
            break

        case 3:
            print(f'Try this exercise: {random.choice(flexibility)}')
            break

        case anything:
            print('Out of range, please enter a number between 1 and 3.')
            print('-------------------------------------------')
            continue