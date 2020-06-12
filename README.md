# pretty_talib
![python_version](https://img.shields.io/static/v1?label=Python&message=3.5%20|%203.6%20|%203.7&color=blue) [![PyPI downloads/month](https://img.shields.io/pypi/dm/pretty_talib?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/pretty_talib)

## Description
Prettified interface for [TA-Lib](https://github.com/mrjbq7/ta-lib)

## Install
1. Install TA-Lib dependency
    - For Mac it's easy as that
      ~~~~shell
      brew install ta-lib
      ~~~~
    - For other platforms, or troubleshooting please check the installation guide for [TA-Lib](https://github.com/mrjbq7/ta-lib)

2. Install pretty_talib
~~~~bash
pip install pretty_talib
# or
pip3 install pretty_talib
~~~~

## Usage
~~~~python
# System
import json

# Pip
import numpy

# Local
from pretty_talib import get_stats, ALL, FunctionName



l=50
timeperiod = 5
data = {
    'open': numpy.random.random(l),
    'high': numpy.random.random(l),
    'low': numpy.random.random(l),
    'close': numpy.random.random(l),
    'volume': numpy.random.random(l)
}

stats = get_stats(data, types=ALL, timeperiod=timeperiod, use_builtin_types=False)

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
~~~~

## Credits
[TA-Lib](https://github.com/mrjbq7/ta-lib) by [mrjbq7](https://github.com/mrjbq7)