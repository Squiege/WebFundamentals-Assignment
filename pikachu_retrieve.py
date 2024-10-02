# Part 1, Task 1, 2, 3
import requests

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}' 
    try:
        response = requests.get(url)
        response.raise_for_status() 
        pokemon = response.json() 

        # Checks if the pokemon is a dictionary
        if isinstance(pokemon, dict):
            name = pokemon.get("name", "no name")
            abilities = pokemon.get("abilities", [])
            weight = pokemon.get("weight", 0) 

            # Pulls the ability names from the dictionary
            ability_names = [ability["ability"]["name"] for ability in abilities]

            # Printing the data to the user
            print(f'Name: {name}')
            print('Abilities:', ', '.join(ability_names))
            print(f'Weight: {weight}')
            print() 
            
            return weight  
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {pokemon_name}: {e}')

    return 0  

def calculate_average_weight(pokemon_names):
    total_weight = 0 # Collects the weights from each pokemon passed through
    count = 0 # Collects the number of pokemon passed through to find the average

    # Grabs each pokemon and their weight
    for pokemon_name in pokemon_names:
        print(f'Fetching data for: {pokemon_name}')
        weight = fetch_pokemon_data(pokemon_name)
        total_weight += weight
        if weight > 0:
            count += 1 

    # If the count is more than 0, finds the average weight of all the pokemon
    if count > 0:
        average_weight = total_weight / count
        print(f'Average Weight: {average_weight}')
    else:
        print('No valid weights to calculate average.')

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

calculate_average_weight(pokemon_names)
