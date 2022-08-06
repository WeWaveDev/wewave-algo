## WeWave Algo

### Contents
1. interface with WeWave API
2. example of how to use WeWave API
3. ready to use algotrading example codes [coming]

### Environment
1. For python developer, WeWave interface only relies on few python library, most stable version of python should work. Recommend: version 3.8
```bash
python3.8 -m venv venv3.8
source venv3.8/bin/activate
python -m pip install requests
```

### Example
1. run 1week(15min interval) and 1 day(5min interval) pattern match realtime result. Feel free to change the parameters of `assetClasses` and `easy_start_screener_id`. You can find `easy_start_screener_id` in the end of each easy start url in wewave.app
```
cd examples-python
python example1.py
```
2. run 2 hour (1 min interval) pattern matching from example2.py
```
cd examples-python
python example2.py
```


### Algo trades execution
1. Algo developer can use any brokerage API you want since WeWave API is generic.
2. Currently we prefer Alpaca API for example code since it is well documented. We also look into TD-Ameritrade API. Feel free to let us know what brokerage API you prefer as example code.

### feedbacks
1. feel free to open ticket or pr
2. email: team@wewave.app
3. Discord: https://discord.gg/Rmpxr9xRY6