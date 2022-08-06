import pprint
from api_interface import get_pattern_result_using_easy_start
pp = pprint.PrettyPrinter(indent=4)


if __name__ == '__main__':

    # Steady Uptrend - crypto, 2hour as pattern range
    (simplified, only_symbol) = get_pattern_result_using_easy_start(assetClasses=["X"], easy_start_screener_id='price-steady-uptrend-2hour')
    print('Steady Uptrend - 1min interval - 2 hour - tickers and data')
    pp.pprint(simplified)
    print('Steady Uptrend - 1min interval - 2 hour - only symbol')
    pp.pprint(only_symbol)
    print('\n\n')

    # Steady Uptrend - crypto, 2hour as pattern range
    (simplified, only_symbol) = get_pattern_result_using_easy_start(assetClasses=["CS"], easy_start_screener_id='price-steady-uptrend-2hour')
    print('Steady Uptrend - 1min interval - 2 hour - tickers and data')
    pp.pprint(simplified)
    print('Steady Uptrend - 1min interval - 2 hour - only symbol')
    pp.pprint(only_symbol)
    print('\n\n')