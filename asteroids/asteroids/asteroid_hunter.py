import os
import json
import requests

def asteroid_closest_approach():
    all_asteroids = []
    # req = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={os.environ["POETRY_NASA_API_KEY"]}')
    # pages = req.json()['page']['total_pages']
    # for pg in range(0, pages):
    asteroids = requests.get(f'http://www.neowsapp.com/rest/v1/neo/browse?page=0&size=20&api_key={os.environ["POETRY_NASA_API_KEY"]}')
    for ast in range(0, 20):
        approaches = asteroids.json()['near_earth_objects'][ast]['close_approach_data']
        closest_approach = min(approaches, key=lambda x:x['miss_distance']['astronomical'])
        all_asteroids.append(asteroids.json()['near_earth_objects'][ast])
        all_asteroids[ast]['close_approach_data'] = [closest_approach]
    return json.dumps(all_asteroids)


#def month_closest_approaches():



#def nearest_misses():
