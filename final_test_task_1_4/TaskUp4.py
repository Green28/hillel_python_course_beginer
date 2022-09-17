import requests

# Class attributes
new_currency: str = "UAH"
old_currency: str = "USD"


def files_bal_uah() -> str:  # Opening the file for reading information
    with open('balans_UAH.txt', 'r') as b_uah:
        b_UAH = b_uah.read()
    return b_UAH


def files_bal_usd() -> str:  # Opening the file for reading information
    with open('balans_USD.txt', 'r') as b_usd:
        b_USD = b_usd.read()
    return b_USD


def rules():
    print(f"COMMAND: \nCOURSE USD or COURSE UAH - Obtaining the current exchange rate. "
          f"\nEXCHANGE USD AMOUNT  or  EXCHANGE UAH AMOUNT - Performs an exchange operation, if the required currency "
          f"is available. \nSTOP - SERVICE STOPPED")


def output():  # Output  information
    data: dict = get_api_data()
    old_currency: str = data["old_currency"]
    old_amount: float = data["old_amount"]
    new_currency: str = data["new_currency"]
    new_amount: float = data["new_amount"]
    currency: float = new_amount / old_amount
    return old_currency, old_amount, new_currency, new_amount, currency


def get_api_data() -> dict:  # Obtaining an actual information UAH and USD
    api_url: str = f'https://api.api-ninjas.com/v1/convertcurrency?want={new_currency}&have={old_currency}&amount=100'
    response = requests.get(api_url, headers={'X-Api-Key': '8EpshFbnnLcCsGK0lfBjJA==ccgvyOu4T2cJObgy'})
    data: dict = response.json()
    if response.status_code == requests.codes.ok:
        return data
    else:
        print("Error:", response.status_code, response.text)


def command_ex():  # Working with software command
    command: str = input()
    while True:
        if "COURSE " in command.upper():
            course(command)
            break
        elif "EXCHANGE " in command.upper():
            exchange(command)
            break
        elif "STOP" == command.upper():
            print("SERVICE STOPPED")
            exit()
        else:
            print(f"INVALID COMMAND - {command} ")
            break


def course(command_course):  # Derivation of the course by command
    bal_UAH: float = float(files_bal_uah())  # Opening the file for reading information
    bal_USD: float = float(files_bal_usd())  # Opening the file for reading information
    if command_course.upper() == "COURSE USD":
        print(f'RATE {round(output()[4], 2)}, AVAILABLE {round(bal_USD, 2)} ')
    elif command_course.upper() == "COURSE UAH":
        print(f'RATE {round((output()[4]) / 1000, 2)}, AVAILABLE {round(bal_UAH, 2)} ')
    else:
        print(f" INVALID CURRENCY {(command_course.split())[-1]}")


def exchange(command_exchange):  # For currency exchange, sale and purchase, with saving and changing the balance in
    # separate text files
    bal_UAH: float = float(files_bal_uah())
    bal_USD: float = float(files_bal_usd())
    amount = int((command_exchange.split(' '))[-1])
    if "EXCHANGE UAH" in command_exchange.upper():

        rate_uah: float = round((output()[4]) / 1000, 2)
        if (bal_USD - (amount * rate_uah)) > 0:
            print(f"USD {bal_USD}, RATE {rate_uah}, amount {amount}")
            with open('balans_UAH.txt', 'w') as b_uah:  # Opening the file to change and record information
                b_uah.write(f'{bal_UAH - amount}')
            with open('balans_USD.txt', 'w') as b_usd:  # Opening the file to change and record information
                b_usd.write(f'{bal_USD + (amount * rate_uah)}')
        else:
            print(
                f" UNAVAILABLE, REQUIRED BALANCE  {round(amount * rate_uah, 2)} USD, AVAILABLE {round(bal_USD, 2)} USD")

    elif "EXCHANGE USD" in command_exchange.upper():
        rate_usd: float = round(output()[4], 2)
        if (bal_UAH - (amount * rate_usd)) > 0:
            print(f"UAH {bal_UAH}, RATE {rate_usd}, amount {amount}")
            with open('balans_USD.txt', 'w') as b_usd:  # Opening the file to change and record information
                b_usd.write(f'{bal_USD - amount}')
            with open('balans_UAH.txt', 'w') as b_uah:  # Opening the file to change and record information
                b_uah.write(f'{bal_UAH + (amount * rate_usd)}')
        else:
            print(
                f"UNAVAILABLE, REQUIRED BALANCE  {round(amount * rate_usd, 2)} UAH, AVAILABLE {round(bal_UAH, 2)} UAH")
    else:
        print(f"INVALID COMMAND ")


def main():  # Collection of all functions together
    rules()
    while True:
        print("COMMAND?")
        command_ex()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Invalid command or missing  correct argument - 'AMOUNT'")
    main()
