import requests
import pprint
import json
pp = pprint.PrettyPrinter(indent=4)
URL_BASE = 'https://j32e1smuxe.execute-api.us-east-1.amazonaws.com/prod'


def get_pattern_result_using_easy_start(assetClasses=["CS", "ETF"], easy_start_screener_id='price-crossover-sma50-1day'):
  patten_setup_request = URL_BASE + '/api/v1/easy-start?screenerId='+easy_start_screener_id
  r = requests.get(url = patten_setup_request)
  screener_config = r.json()

  search_url = URL_BASE + '/api/v1/search'
  search_payload = {
    "searchId": None,
    "traditionalScreener": {
        "filterBySymbolType": assetClasses,
        # "filterByCapsize": {
        #     "gte": 1000 # 1M is the unit. greater than 1 billion market cap
        # },
    },
    "trendScreener": {
        "sketchRange":  screener_config['data']['Item']['traditionalScreener']['sketchRange'],
        "trendArray": screener_config['data']['Item']['trendlineObject']['trendline'],
    }
  }
  if screener_config['data']['Item']['traditionalScreener']['sketchRange'] == '2H':
        search_payload['trendScreener']['timeInterval'] = '1MIN'
  if screener_config['data']['Item']['traditionalScreener']['sketchRange'] == '2H':
        search_payload['trendScreener']['sketchRange'] = 120

#   pp.pprint(search_payload)

  #execute search
  r = requests.post(url = search_url, data = json.dumps(search_payload))
  data = r.json()

  simplified = []
  only_symbol= []
  for obj in data['result']:
      simplified.append({
          "symbol": obj['symbol'],
          "price": obj['price'],
          "volume": int(obj['volume']),
          'closePriceChangeRatio':  obj['closePriceChangeRatio'],
          'similarity': obj['similarity'],
      })
      only_symbol.append(obj['symbol'])
  return (simplified, only_symbol)
