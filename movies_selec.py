"""Elegir una película para ver puede ser una lucha, especialmente con tantas opciones disponibles.
En este proyecto, crearás un programa Python simple que sugiere una película al azar según el género
que seleccione el usuario. El programa utilizará un diccionario predefinido de películas y géneros, 
lo que permitirá a los usuarios obtener una recomendación rápida sin tener que desplazarse sin fin."""

import datetime
import random


movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

print(" Action\n", "Comedy\n", "Drama\n", "Sci-fi\n","Horror\n")
# Obtener el género deseado por el usuario
user_genre = input("Enter your favorite genre: ").title()
user_genre = user_genre.strip()

while True:
    match user_genre:

        case 'Action':
            movie = random.choice(movies['Action'])
            print(f"Based on your preference, I recommend watching '{movie}'.")
            break

        case 'Comedy':
            movie = random.choice(movies['Comedy'])
            print(f"Based on your preference, I recommend watching '{movie}'.")
            break

        case 'Drama':
            movie = random.choice(movies['Drama'])
            print(f"Based on your preference, I recommend watching '{movie}'.")
            break

        case 'Sci-Fi':
            movie = random.choice(movies['Sci-Fi'])
            print(f"Based on your preference, I recommend watching '{movie}'.")
            break

        case 'Horror':
            movie = random.choice(movies['Horror'])
            print(f"Based on your preference, I recommend watching '{movie}'.")
            break

        case anything:
            print("Invalid genre, please try again.")
            user_genre = input("Enter your favorte genre: ")
            continue