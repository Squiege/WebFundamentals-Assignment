import requests

def fetch_planet_data():
    # Enhance format the output in a more readable manner
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get("englishName")#get planet English name
            mass = planet.get("mass", []).get("massValue") #get planet mass
            orbit_period = planet.get("sideralOrbit")#get planet orbit period
            print(f"Planet: {name}\n Mass: {mass}\n Orbit Period: {orbit_period} days")
            print(" ")
    return planets#list of planets

def find_heaviest_planet(planets):
    heaviest_planet = None  # Variable to keep track of the heaviest planet
    max_mass = 0  # Variable to keep track of the maximum mass

    for planet in planets:
        if planet.get('isPlanet', False):
            name = planet.get("englishName")  
            mass_info = planet.get("mass", {})  
            
            # Checking if the mass is a dictionary
            if isinstance(mass_info, dict):
                mass_value = mass_info.get("massValue", 0)  # Get mass value
                mass_exponent = mass_info.get("massExponent", 0)  # Get mass exponent
                
                # Calculate mass in kilograms, equation is mass = massValue x 10(to the power of the exponent)
                mass = mass_value * (10 ** mass_exponent)

                orbit_period = planet.get("sideralOrbit")  # Get planet orbit period

                # Print planet details
                print(f"Planet: {name}\nMass: {mass} kg\nOrbit Period: {orbit_period} days\n")

                # Check if the planet is the heaviest and if it is set the heaviest planet to the name of the planet
                if mass > max_mass:
                    max_mass = mass
                    heaviest_planet = name

    if heaviest_planet:
        return heaviest_planet, max_mass  # Return name and mass of the heaviest planet
    else:
        print("No planets found.")
        return None, 0  # Return None and 0 if no planets found

# Fetch planets and then find the heaviest
planets = fetch_planet_data()
heaviest_name, heaviest_mass = find_heaviest_planet(planets)

# Prints out the heaviest planet after going through each planet
if heaviest_name:
    print(f"The heaviest planet is {heaviest_name} with a mass of {heaviest_mass} kg.")

