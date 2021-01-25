import json
from asteroids.asteroid_hunter import asteroid_closest_approach
# import asteroids.asteroid_hunter.month_closest_approaches
# import asteroids.asteroid_hunter.nearest_misses

def test_only_one_closest_approach():
    result = json.loads(asteroid_closest_approach())[0]
    assert 'close_approach_data' in result
    assert len(result['close_approach_data']) == 1
