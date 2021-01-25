import os
import json
import requests

def asteroid_closest_approach():
    all_asteroids = []
    req = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={os.environ["POETRY_NASA_API_KEY"]}')
    pages = req.json()['page']['total_pages']
    for pg in range(0, 5):
    #set to range(0, pages) for all data - didn't want to rate limit while testing
        asteroids = requests.get(f'http://www.neowsapp.com/rest/v1/neo/browse?page={pg}&size=20&api_key={os.environ["POETRY_NASA_API_KEY"]}')
        for ast in range(0, 20):
            approaches = asteroids.json()['near_earth_objects'][ast]['close_approach_data']
            closest_approach = min(approaches, key=lambda x:x['miss_distance']['astronomical'])
            all_asteroids.append(asteroids.json()['near_earth_objects'][ast])
            all_asteroids[((pg * 20) + ast)]['close_approach_data'] = [closest_approach]
    return json.dumps(all_asteroids)


def month_closest_approaches():
    element_count = 0
    near_earth_objects = {}
    calendar = [['01-01','01-08'], ['01-09','01-15'], ['01-16','01-22'], ['01-23','01-29'], ['01-30','01-31']]
    for week in calendar:
        weekly_approaches = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-{week[0]}&end_date=2021-{week[1]}&api_key={os.environ["POETRY_NASA_API_KEY"]}')
        element_count += weekly_approaches.json()['element_count']
        near_earth_objects.update(weekly_approaches.json()['near_earth_objects'])
    month_approaches = {'element_count' : element_count} | {'near_earth_objects' : near_earth_objects}
    return json.dumps(month_approaches)

#def nearest_misses():
