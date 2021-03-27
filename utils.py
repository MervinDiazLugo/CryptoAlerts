import null as null
from openpyxl import load_workbook
import requests
import json
from datetime import datetime, timedelta

PLAZO = 60
PORCENTAJE = 20
DESDE = (datetime.utcnow() - timedelta(days = PLAZO)).timestamp()
HASTA  = datetime.utcnow().timestamp()
EXCEL_FILE ='./template/Crypto.xlsx'
EXCEL_FILE_OUTPUT ='./output/Crypto_Copy.xlsx'
HOJA= "Hoja1"
COIN_LIST = []
retrieve_coin={}
ESPERADO = ""

class Utils:

    def workbook(self, excel_file=EXCEL_FILE):
        global wb
        wb = load_workbook(excel_file)
        return wb

    def load_sheet(self, excel_file=EXCEL_FILE, hoja=HOJA):
        excel = Utils.workbook(excel_file)
        ws = excel[hoja]
        return ws

    def retrieve_coin_estimated_volume(self, id):
        total_volumes = json.loads(requests.get(
            f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency=usd&days={PLAZO}&interval=daily").text)

        avg = 0
        volume = total_volumes['total_volumes']
        count = 0
        for vol in volume:
            avg = avg + vol[1]
            count = count + 1

        avg = avg / count
        return avg

    def retrieve_coin_data(self, excel_file=EXCEL_FILE, hoja=HOJA,  estimaciones=[]):
        sheet = Utils.load_sheet(excel_file, hoja)
        row = 2
        count = 0
        for coin in estimaciones:
            try:
                coin_data = json.loads(requests.get(
                    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={}&order=market_cap_desc&per_page=100&page=1&sparkline=false".format(
                        coin)).text)
                coin_data = coin_data[0]
                retrieve_coin["id"] =coin_data['id']
                retrieve_coin["current_price"] = coin_data['current_price']
                retrieve_coin["market_cap"] = coin_data['market_cap']
                retrieve_coin["circulating_supply"] = coin_data['circulating_supply']
                retrieve_coin["total_volume"] = coin_data['total_volume']
                retrieve_coin["real_market_price"] = coin_data['market_cap'] / coin_data['circulating_supply']
                retrieve_coin["diferencial"] = retrieve_coin["real_market_price"] - coin_data['current_price']
                retrieve_coin["volumen_avg"] = Utils.retrieve_coin_estimated_volume(self, coin_data['id'])

                if coin_data['total_volume'] >= retrieve_coin["volumen_avg"]:
                    ESPERADO = "ALTA"
                else:
                    ESPERADO = "BAJA"
                retrieve_coin["expectativa"] = ESPERADO

                barrera = coin_data["total_volume"] + int((coin_data["total_volume"]*(PORCENTAJE))/100)
                if barrera>=int(retrieve_coin["volumen_avg"]):
                    ALERTA = "ALERTA"
                else:
                    ALERTA = ""
                retrieve_coin['Alerta'] = ALERTA
                print(retrieve_coin)

                for col, value in enumerate(retrieve_coin.values(), start=1):
                    sheet.cell(row=row, column=col).value = value
                    sheet.cell(row=row, column=col).number_format = '#,##0.000000000'
                wb.save(EXCEL_FILE_OUTPUT)
                row = row+1
                count = count + 1
            except (IndexError, KeyError, ValueError) as error:
                print(error)
                continue


