from utils import Utils
utils = Utils()

estimaciones = [
    'bitcoin',
    'ethereum',
    'binancecoin',
    'vechain',
    'chiliz',
    'cardano',
    'filecoin',
    'eos',
    'ankr',
    'metal'
     ]
utils.retrieve_coin_data(estimaciones=estimaciones)

#utils.retrieve_coin_data(self, estimaciones=utils.retrieve_coin_list(self))

#utils.retrieve_coin_data(hoja="Trends", estimaciones=utils.retrieve_coin_trend())
