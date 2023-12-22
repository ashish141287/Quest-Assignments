''' get different data from str wars films and starships'''

import requests


def get_ships_from_return_of_jedi():
    '''Get all the statships that appeared in Return of the Jedi'''
    #film URL from starwars
    film_url = "https://swapi.dev/api/films"
    data = requests.get(film_url, timeout=60).json()

    for film in data["results"]:
        if film['title'] == "Return of the Jedi":
            starships_in_jedi = film["starships"]

    for ship in starships_in_jedi:
        starship_response = requests.get(ship, timeout=60).json()

        print(f"starShip Name: {starship_response['name']}")


def get_ships_with_hyperdrive_rating():
    '''Get all the statships that have a hyperdrive rating >= 1.0'''
    #Starship URL from starwars
    starship_url = "https://swapi.dev/api/starships"
    starship_data = requests.get(starship_url, timeout=60).json()

    for starship in starship_data["results"]:
        if float(starship['hyperdrive_rating']) >= 1.0:
            print(f"starShip with Hyperdrive Rating: {starship['name']}")


def get_crew_between_3_100():
    '''Get all the ships that have crews between 3 and 100'''
    #Starship URL from starwars
    starship_url = "https://swapi.dev/api/starships"
    starship_data = requests.get(starship_url, timeout=60).json()

    for starship in starship_data["results"]:
        if 3 <= int(starship['crew']) <= 100:
            print(f"Crew Name: {starship['name']}")


if __name__ == "__main__":
    get_ships_from_return_of_jedi()
    get_ships_with_hyperdrive_rating()
    get_crew_between_3_100()
