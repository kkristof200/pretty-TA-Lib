from pretty_talib import get_stats, FunctionName, ALL
import numpy as np
from funcmeasure import measure

# note that all ndarrays must be the same length!
full_len=50
tf = 20
tp = 5

inputs = {
    'open': np.random.random(full_len),
    'high': np.random.random(full_len),
    'low': np.random.random(full_len),
    'close': np.random.random(full_len),
    'volume': np.random.random(full_len)
}

# res = get_stats(inputs, timeperiod=tp, map_results=True)
# print(res)

def f1():
    get_stats(inputs, timeperiod=tp, map_results=False)

def f2():
    get_stats(inputs, timeperiod=tp, map_results=True)

measure([f1, f2], times=100)