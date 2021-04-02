from utils import Utils
import sys
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
    'decentraland',
    'Siacoin',
    'moviebloc',
    'stp-network',
    'link',
    'uniswap',
    'theta-network',
    'bidr',
    'superfarm'
     ]

arguments = sys.argv

for args in arguments:
        if args == "Trend":
            utils.retrieve_coin_data(estimaciones=utils.retrieve_coin_trend(), output='./output/Trend.xlsx')

        if args == "Estimated":
            utils.retrieve_coin_data(estimaciones=estimaciones, output='./output/Estimated.xlsx')

        if args == "All":
            utils.retrieve_coin_data(estimaciones=utils.retrieve_coin_list(), baja=True)



#utils.retrieve_coin_data(hoja="Trends", estimaciones=utils.retrieve_coin_trend(), baja=True, output='./output/trend.xlsx')


