from self import self

from utils import Utils

estimaciones = [
    'bitcoin',
    'ethereum',
    'binancecoin',
    'vechain',
    'chiliz',
    'cardano',
    'filecoin',
    'eos',
    'fusion',
    'safemoon'
     ]
#Utils.retrieve_coin_data(self, estimaciones=estimaciones)

Utils.retrieve_coin_data(self, estimaciones=Utils.retrieve_coin_list(self))

