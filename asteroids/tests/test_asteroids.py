import json
from asteroids.asteroid_hunter import asteroid_closest_approach
# import asteroids.asteroid_hunter.month_closest_approaches
# import asteroids.asteroid_hunter.nearest_misses

#for these tests to work, you need to set pages = 5 in the method - because of
#how many pages there are in the data, didn't want to end up limiting my api key
def test_only_one_closest_approach():
    result = json.loads(asteroid_closest_approach())[0]
    assert 'close_approach_data' in result
    assert len(result['close_approach_data']) == 1

def test_multiple_pages_of_closest_approach():
    result = json.loads(asteroid_closest_approach())
    assert len(result) == 100
    assert result[0]['id'] == '2000433'
    assert result[-1]['id'] == '2005660'
