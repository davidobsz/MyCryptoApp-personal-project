from pycoingecko import CoinGeckoAPI
import datetime
import time
cg = CoinGeckoAPI()


price = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
#print(price)


data = cg.get_coin_history_by_id(id='bitcoin',date='11-11-2021', localization='false')
print(data)
print(data["market_data"]["current_price"]["usd"])
history = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='1')
#print(history["prices"][-1])
print(history["prices"])
# while True:
#     # prints latest bitcoin price
#     history = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='1')
#     #print(len(history["prices"]), history["prices"][-1])
#     print(history["prices"])
#     # Wait for some amount of seconds
#     time.sleep(1)