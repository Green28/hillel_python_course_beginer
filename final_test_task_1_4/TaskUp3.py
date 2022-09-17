import requests
import click


class Uah:
    # Class attributes
    line1: str = "--------------"
    line2: str = "=============="

    def __init__(self, currency: str, data=None):
        self.currency: str = currency.upper()
        self.data: str = data

    def output(self):  # Output  information
        data_uah: list = self.choose_data()
        data_uah: dict = data_uah[0]
        currency: str = data_uah['cc']
        rate: int = data_uah['rate']
        print(f'{Uah.line1}\n{currency}\n\n{rate}\n{Uah.line2}')

    def choose_data(self):  # Choice of method, with or without a date argument
        if self.data == None:
            return self.get_api_currency_today()
        else:
            return self.get_api_currency_same()

    def get_api_currency_today(self) -> list:  # Obtaining the exchange rate for today, without entering the date
        api_url_currency: str = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?valcode={self.currency}&json'
        response_currency: any = requests.request("GET", api_url_currency)
        data: list = response_currency.json()
        if len(data) != 0:
            return data
        else:
            raise SystemError

    def get_api_currency_same(self) -> list:  # Obtaining the exchange rate for a specific date, with date input.
        check_date: str = self.data
        self.data: str = str(self.data).replace('-', '')
        api_url_currency: str = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?valcode={self.currency}&date={self.data}&json'
        response_currency: any = requests.request("GET", api_url_currency)
        data: list = response_currency.json()
        if bool(data) != False:
            if len(data[0]) > 1:
                return data
            else:
                print(f"Invalid currency or date: {check_date}")
                exit()
        else:
            print(f"Invalid date : {self.currency}")
            exit()


if __name__ == "__main__":
    @click.command()
    @click.argument('currency')
    @click.option('--data', '-d')
    def exemplar(currency, data=None):
        _ = Uah(currency, data)
        return _.output()


    exemplar()
