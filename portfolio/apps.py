from django.apps import AppConfig
import socket
import json
import asyncio
import websockets
from decimal import Decimal
import threading
import websocket

import asyncio
import asyncws


class ApiWebSocket(object):

    def __init__(self):
        self.BASE_URL = 'wss://portal.coinroutes.com/api/'
        self.SOR_TOKEN = '6c634e1eacecc4801b000249287fbf923d5c8824'

    @asyncio.coroutine
    def echo(self):
        query = {"currency_pair": "BTC-USD", "size_filter": "0.00", "sample": 1}
        websocket = yield from asyncws.connect(self.url())
        while True:
            yield from websocket.send('hello')
            echo = yield from websocket.recv()
            if echo is None:
                break
            print(echo)

    def url(self):
        return "{}streaming/cbbo/?token={}".format(self.BASE_URL, self.SOR_TOKEN)

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.echo())
        asyncio.get_event_loop().close()

# class ApiWebSocket(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.BASE_URL = 'wss://portal.coinroutes.com/api/'
#         self.SOR_TOKEN = '6c634e1eacecc4801b000249287fbf923d5c8824'
#         self.exchanges = ['gdax', 'gemini', 'kraken', 'bitstamp', 'b2c2', 'cumberland', 'hehmeyer', 'binance']
#         self.currency_pairs = {}
#         self.prices = {}
#         # self.FUNDING_CCY = "USD"  # change this to your desired base
#         self.sample_pairs = [
#             'BTC-AUD', 'ETH-AUD', 'LTC-AUD', 'XRP-AUD', 'BCH-AUD', 'USDT-AUD', 'EOS-AUD', 'XLM-AUD', 'DOT-AUD',
#             'LINK-AUD', 'USDC-AUD', 'BSV-AUD', 'ADA-AUD', 'DOGE-AUD', 'BTC-USD'
#         ]
#
#     @property
#     def url(self):
#         return "{}streaming/cbbo/?token={}".format(self.BASE_URL, self.SOR_TOKEN)
#
#     def _best_side(self, side):
#         side_data =  [i for i in side if i['exchange'] in self.exchanges]
#         if len(side_data):
#             return side_data[0]
#         return None
#
#     def _process_cbbo(self, message):
#         currency, funding = message['product'].split('-')
#         best_bid, best_ask = self._best_side(message['bids']), self._best_side(message['asks'])
#         if best_bid and best_ask:
#             price = self.currency_pairs[message['product']] =  str((Decimal(best_ask['price']) + Decimal(best_bid['price'])) / 2)
#             print(f'Price of {message["product"]}: {price}')
#             # if funding == self.FUNDING_CCY:
#             #     self.prices[currency] = price
#
#     async def _connect_currency(self, pair):
#         print("connect {} {}".format(pair, self.url))
#         while True:
#             try:
#                 async with websockets.connect(self.url, timeout=30, max_queue=1000 ) as websocket:
#                     query = {"currency_pair":pair,"size_filter":"0.00","sample":1}
#                     print("ws connect {} {}".format(pair, self.url))
#                     await websocket.send(json.dumps(query))
#                     print(" {} data loop".format(pair))
#                     while True:
#                         message = json.loads(await websocket.recv())
#                         if message.get('errors'):
#                             print(message)
#                             await asyncio.sleep(60)
#                         else:
#                             self._process_cbbo(message)
#             except websockets.exceptions.InvalidStatusCode as e:
#                 if e.status_code == 403:
#                     print("Rate limited {}, sleeping".format(pair))
#                     await asyncio.sleep(60)
#             except Exception as e:
#                 import traceback; traceback.print_exc()
#
#     async def connect_endpoints(self):
#         futures = [asyncio.ensure_future(self._connect_currency(pair)) for pair in self.sample_pairs]
#         await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
#
#     def run(self):
#         event_loop = asyncio.new_event_loop()
#         event_loop.run_until_complete(self.connect_endpoints())

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    # ApiWebSocket().run()