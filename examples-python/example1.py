import pprint
from api_interface import get_pattern_result_using_easy_start
pp = pprint.PrettyPrinter(indent=4)


if __name__ == '__main__':
    # cross over - common stock and etf, 1week as pattern range
    (simplified, only_symbol) = get_pattern_result_using_easy_start(assetClasses=["CS", "ETF"], easy_start_screener_id='price-crossover-sma50-1week')
    print('Momentum Crossing MA 50 - 15min interval - 1 week - tickers and data')
    pp.pprint(simplified)
    print('Momentum Crossing MA 50 - 15min interval - 1 week - only symbol')
    pp.pprint(only_symbol)
    print('\n\n')

    # cross over sma 50 - common stock and etf, 1day as pattern range
    (simplified, only_symbol) = get_pattern_result_using_easy_start(assetClasses=["CS", "ETF"], easy_start_screener_id='price-crossover-sma50-1day')
    print('Momentum Crossing MA 50 - 5min interval - 1 day - tickers and data')
    pp.pprint(simplified)
    print('Momentum Crossing MA 50 - 5min interval - 1 day - only symbol')
    pp.pprint(only_symbol)
    print('\n\n')

    # cross over - common stock and etf, 2hour as pattern range
    (simplified, only_symbol) = get_pattern_result_using_easy_start(assetClasses=["CS", "ETF"], easy_start_screener_id='price-crossover-sma50-2hour')
    print('Momentum Crossing MA 50 - 1min interval - 2 hour - tickers and data')
    pp.pprint(simplified)
    print('Momentum Crossing MA 50 - 1min interval - 2 hour - only symbol')
    pp.pprint(only_symbol)
    print('\n\n')


    # Steady Uptrend - common stock and etf, 1week as pattern range
    (simplified, only_symbol) = get_pattern_result_using_easy_start(assetClasses=["CS"], easy_start_screener_id='price-steady-uptrend-1week')
    print('Steady Uptrend - 15min interval - 1 week - tickers and data')
    pp.pprint(simplified)
    print('Steady Uptrend - 15min interval - 1 week - only symbol')
    pp.pprint(only_symbol)
    print('\n\n')