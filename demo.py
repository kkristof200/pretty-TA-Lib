# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import json

# Pip
import numpy

# Local
from pretty_talib import get_stats, ALL, FunctionName

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------------- Flow ----------------------------------------------------------------- #

l=50
timeperiod = 5
data = {
    'open': numpy.random.random(l),
    'high': numpy.random.random(l),
    'low': numpy.random.random(l),
    'close': numpy.random.random(l),
    'volume': numpy.random.random(l)
}

stats = get_stats(data, timeperiod=timeperiod, use_builtin_types=True)

with open('stats.json', 'w') as file:
    json.dump(stats, file, indent=4)

# BENCHMARKS

# from funcmeasure import measure

# def use_objects_false_use_builtin_types_false():
#     get_stats(data, types=ALL, timeperiod=timeperiod)

# def use_objects_false_builtin_types_true():
#     get_stats(data, types=ALL, timeperiod=timeperiod, use_builtin_types=True)

# def use_objects_true_use_builtin_types_true():
#     get_stats(data, types=ALL, timeperiod=timeperiod, use_objects=True)

# measure(
#     [
#         use_objects_false_use_builtin_types_false,
#         use_objects_false_builtin_types_true,
#         use_objects_true_use_builtin_types_true
#     ],
#     times=100
# )


# ---------------------------------------------------------------------------------------------------------------------------------------- #