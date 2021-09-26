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

    async def get_data(self, query):
        async with websockets.connect(self.url) as websocket:
            await websocket.send(query)
            content = await websocket.recv()
            print(f'Content: {content}')

    @property
    def url(self):
        return "{}streaming/cbbo/?token={}".format(self.BASE_URL, self.SOR_TOKEN)

    def run(self, query):
        event_loop = asyncio.new_event_loop()
        event_loop.run_until_complete(self.get_data(query))

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'