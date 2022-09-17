import requests
import click


class CityWorld:
    # Class attributes
    line1: str = "--------------"
    line2: str = "=============="
    headers: dict = {'X-Api-Key': '8EpshFbnnLcCsGK0lfBjJA==ccgvyOu4T2cJObgy'}

    def __init__(self, city):
        self.city = city

    def output(self):  # Output of final information
        data_city: dict = self.get_api_city()
        for city in data_city:
            city_name: str = city['name']
            city_id: str = city['country']
            population: int = city['population']
            data_country: dict = self.get_api_country(city_id)
            country: str = data_country['name']
            currency: str = data_country['currency']['code']
            print(f'{CityWorld.line1}\n{city_name}\n\n{population}\n{country}\n{currency}\n{CityWorld.line2}')

    def get_api_city(self) -> dict:  # Getting information about the city
        api_url_city: str = f'https://api.api-ninjas.com/v1/city?name={self.city}&limit=10'
        responses_city: any = requests.get(api_url_city, headers=CityWorld.headers)
        data_city: dict = responses_city.json()
        if responses_city.status_code == 200 and len(responses_city.text) != 2:
            return data_city
        else:
            print(f"Invalid city name: {self.city}")
            exit()

    @staticmethod
    def get_api_country(city_id) -> dict:  # Obtaining information by country, through "city_id"
        api_url_country: str = f'https://api.api-ninjas.com/v1/country?name={city_id}'
        response_country: any = requests.get(api_url_country, headers=CityWorld.headers)
        data_country: list = response_country.json()
        if response_country.status_code == 200:
            country_data: dict = data_country[0]
            return country_data
        else:
            print(f"Error:", response_country.status_code, response_country.text)
            exit()


if __name__ == "__main__":
    @click.command()
    @click.argument('city')
    def exemplar(city):
        try:
            a = CityWorld(city)
            return a.output()
        except Exception:
            print(f"SystemError")


    exemplar()
