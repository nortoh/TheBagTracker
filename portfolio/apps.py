from django.apps import AppConfig
import socket
import json
import asyncio
from decimal import Decimal
import threading
import requests


class ApiWebSocket(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.BASE_URL = 'https://portal.coinroutes.com/api'
        self.SOR_TOKEN = '6c634e1eacecc4801b000249287fbf923d5c8824'

    def run(self, type):
        print('Hello')
        self.rest_call(type)

    def url(self, type):
        return "{}{}?token={}".format(self.BASE_URL, type, self.SOR_TOKEN)

    def rest_call(self, type):
        call = self.url(type)
        print(f'Attempting for {call}')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token 6c634e1eacecc4801b000249287fbf923d5c8824',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

        data = {
              "currency_pair": "BTC-USD",
              "exchanges": [
                "binance"
              ],
              "side": "bids",
              "quantity": 1,
              "use_fees": True,
              "use_funding_currency": False
        }
        response = requests.get(call, headers=headers, data=data)
        print(f'Response: {response.content}')

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'