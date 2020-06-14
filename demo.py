# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import json

# Pip
import numpy

# Local
from pretty_talib import get_stats, ALL, FunctionName

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------------- Flow ----------------------------------------------------------------- #

l=2
timeperiod = 5
data = {
    'open': numpy.random.random(l),
    'high': numpy.random.random(l),
    'low': numpy.random.random(l),
    'close': numpy.random.random(l),
    'volume': numpy.random.random(l)
}

import pandas as pd

df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close', 'volume'])

print(df)

# stats = get_stats(data, timeperiod=timeperiod, use_builtin_types=True)

# with open('stats.json', 'w') as file:
#     json.dump(stats, file, indent=4)

# BENCHMARKS

# from funcmeasure import measure

# def dict_use_objects_false_use_builtin_types_false():
#     get_stats(data, timeperiod=timeperiod)

# def dict_use_objects_false_builtin_types_true():
#     get_stats(data, timeperiod=timeperiod, use_builtin_types=True)

# def dict_use_objects_true_use_builtin_types_true():
#     get_stats(data, timeperiod=timeperiod, use_objects=True)

# def df_use_objects_false_use_builtin_types_false():
#     get_stats(data, timeperiod=timeperiod, use_objects=True)

# measure(
#     [
#         dict_use_objects_false_use_builtin_types_false,
#         dict_use_objects_false_builtin_types_true,
#         dict_use_objects_true_use_builtin_types_true,
#         df_use_objects_false_use_builtin_types_false
#     ],
#     times=250
# )


# ---------------------------------------------------------------------------------------------------------------------------------------- #