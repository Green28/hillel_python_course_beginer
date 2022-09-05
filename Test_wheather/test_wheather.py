from main import World_wheather



def setUp():
    test_weather = World_wheather()
    return test_weather


def test_weather_funk():
    test_weather = setUp()
    try:
        assert test_weather.city.isalpha(), " Only str"
        assert len(test_weather.city) != 1 and len(test_weather.city) != 2, "Too short city`s name"
        assert test_weather.r_data["cod"] != "404", " This city not found"
    except AssertionError as e:
        return f'test_weather is failed error: {e}'
    return "funk weather work"


if __name__ == '__main__':
    print(test_weather_funk())
