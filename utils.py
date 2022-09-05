import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(cur1: str, cur2: str, amount: str):


        if cur1 == cur2:
            raise ConvertionException(f'Невозможно пеевести одинаковые валюты {cur2}.')

        try:
            cur1_ticker = keys[cur1]
        except KeyError:
            raise ConvertionException(f'Не удалось обрработать валюту {cur1}')

        try:
            cur2_ticker = keys[cur2]
        except KeyError:
            raise ConvertionException(f'Не удалось обрработать валюту {cur2}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={cur1_ticker}&tsyms={cur2_ticker}')
        total_cur2 = json.loads(r.content)[keys[cur2]]

        return total_cur2
