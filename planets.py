import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get("englishName")#get planet English name
            mass = planet.get("mass", []) #get planet mass
            mass_value = [mv["massValue"] for mv in mass]
            orbit_period = planet.get("sideralOrbit")#get planet orbit period
            print(f"Planet: {name}, Mass: {mass_value}, Orbit Period: {orbit_period} days")

fetch_planet_data()

