import requests
from decimal import *
from datetime import datetime


getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None

    rur = response[response.find('Value', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(rur.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('GBP'))

