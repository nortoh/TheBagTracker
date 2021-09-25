import asyncio
import websockets

class CoinRoutesAPI(object):

    def __init__(self):
        self.token = '6c634e1eacecc4801b000249287fbf923d5c8824'
        self.ws_url = 'wss://staging.coinroutes.com/api/streaming/cbbo/'

# const ws = new WebSocket('wss://staging.coinroutes.com/api/streaming/cbbo/?token=6c634e1eacecc4801b000249287fbf923d5c8824', []); ws.onopen = () => {     let requestMessage = {         currency_pair: 'BTC-USD',         size_filter: 0,         sample: 0.5,         };         ws.send(JSON.stringify(requestMessage));     };