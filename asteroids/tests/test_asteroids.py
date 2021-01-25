import json
from asteroids.asteroid_hunter import asteroid_closest_approach
from asteroids.asteroid_hunter import month_closest_approaches
from asteroids.asteroid_hunter import nearest_misses

#for these tests to work, you need to set pages = 5 in the asteroid_closest_approach method
#given how many pages there are in the data, didn't want to end up limiting my api key
def test_only_one_closest_approach():
    result = json.loads(asteroid_closest_approach())[0]
    assert len(result['close_approach_data']) == 1

def test_is_minimum_closest_approach():
    result = json.loads(asteroid_closest_approach())[0]
    assert result['close_approach_data'][0]['miss_distance']['astronomical'] == '0.1494623118'

def test_multiple_pages_of_closest_approach():
    result = json.loads(asteroid_closest_approach())
    assert len(result) == 100
    assert result[0]['id'] == '2000433'
    assert result[-1]['id'] == '2005660'

def test_all_days_in_month_closest_approaches():
    result = json.loads(month_closest_approaches())
    assert len(result['near_earth_objects']) == 31

def test_correct_element_count_in_month_closest_approaches():
    result = json.loads(month_closest_approaches())
    sum_of_days = 0
    for day in result['near_earth_objects']:
        sum_of_days += len(result['near_earth_objects'][day])
    assert result['element_count'] == sum_of_days

def test_top_ten_nearest_misses():
    result = json.loads(nearest_misses())
    assert len(result) == 10

def test_nearest_misses_are_smallest():
    result = json.loads(nearest_misses())
    nearest = result[0]['close_approach_data'][0]['miss_distance']['astronomical']
    assert nearest == '0.0045430856'
    assert nearest < result[1]['close_approach_data'][0]['miss_distance']['astronomical']
