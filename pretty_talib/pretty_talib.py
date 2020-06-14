# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, List, Dict, Union, Tuple, Any

# Pip
from jsoncodable import JSONCodable

from talib import abstract
import pandas
import numpy

# Local
from .enums.function_name import FunctionName

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

__ALL_METHODS_KEY = 'ALL'
ALL = __ALL_METHODS_KEY

# Supports 'ALL' as type
def get_stats(
    data: Union[Dict[str, numpy.ndarray], Dict[str, pandas.Series], pandas.DataFrame],
    functions: Dict[Union[FunctionName, str], Tuple[Optional[Tuple], Optional[Dict[str, Any]]]] = {__ALL_METHODS_KEY: (None, None)},
    timeperiod: Optional[int] = None,
    use_builtin_types: bool = False,
    use_objects: bool = False,
) -> Optional[Union[Dict[str, Union[List[numpy.ndarray], numpy.ndarray, pandas.DataFrame]], object]]:
    """Creates TA data for the selected types of analysises

    Args:
        data (Union[Dict[str, numpy.ndarray], Dict[str, pandas.Series], pandas.DataFrame]):
        The data to analyze. Either a dict of numpy.ndarray or pandas.Series, or a pandas.DataFrame.
        If a pandas.DataFrame is provided, the output is returned as a Dict[str, pandas.DataFrame] with named output columns for each.
        For dict, it should look like:
        {
            'open': numpy.ndarray,
            'high': numpy.ndarray,
            'low': numpy.ndarray,
            'close': numpy.ndarray,
            'volume': numpy.ndarray,
        }

        functions (Dict[Union[FunctionName, str], Tuple[Optional[Tuple], Optional[Dict[str, Any]]]]):
        The analysis types, you want to perform Each with args and kwargs.
        Example: {
            FunctionName.STOCH: (
                (5, 3, 0, 3, 0,),
                {
                    prices: ['high', 'low', 'open']
                }
            )
        }
        This would equal to STOCH(inputs, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])
        Defaults to {ALL: (None, None)}.

        timeperiod (int, optional): Time period to calculate analysis with. Will e set only for those functions,
                                    which do not specify timeperiod explicitaly.
                                    Defaults to 30.

        use_builtin_types (bool, optional): returns python list and int/float instead of numpy types.
                                            Defaults to False.

        use_objects (bool, optional): returns oject instead of Dict.
                                      If True, 'use_builtin_types' will be also True.
                                      Defaults to False.

        IMPORTANT NOTE:
            - THE VALUES OF 'use_builtin_types' AND 'use_objects' HIGHLY AFFECTS EFFICIENCY
              SEE BENCHMARK BELOW (Ran 250 times)

            --------------------------------------------------------------------------
            | rank |                    name                    |  duration  |  perc |
            --------------------------------------------------------------------------
            |    1 | use_builtin_types=False, use_objects=False | 0.00626893 |       |
            |    2 |  use_builtin_types=True, use_objects=False | 0.02440002 | 3.89x | -> ~4x slower
            |    3 |   use_builtin_types=True, use_objects=True | 0.03171391 | 5.05x | -> ~5x slower
            --------------------------------------------------------------------------

    Returns:
        Optional[Union[Dict[str, Any], object]]: Returns dictionary or objects, based on the provided values for 'use_builtin_types' and 'use_objects'
    """

    if isinstance(data, pandas.DataFrame):
        use_builtin_types = False
        use_objects = False

    if __ALL_METHODS_KEY in functions.keys():
        params = functions[__ALL_METHODS_KEY]

        for func_name_enum in FunctionName:
            if func_name_enum not in functions:
                functions[func_name_enum] = params

        del functions[__ALL_METHODS_KEY]

    res = {}

    for func_name_enum, args_kwargs in functions.items():
        func_name = func_name_enum.value
        func = abstract.Function(func_name)

        args, kwargs = args_kwargs
        k_timeperiod = 'timeperiod'

        args = (data,) if args is None else (data,) + args
        kwargs = kwargs or { k_timeperiod: timeperiod }

        if k_timeperiod not in kwargs:
            kwargs[k_timeperiod] = timeperiod

        try:
            _res = func(*args, **kwargs)

            if (use_builtin_types or use_objects):
                _res = __convert_to_builtin(_res)

            res[func_name] = _res
        except Exception as e:
            print(func_name, e)

    return res if not use_objects else JSONCodable.from_json(res)


# ----------------------------------------------------------- Private methods ------------------------------------------------------------ #

def __convert_to_builtin(numpy_list) -> List:
    new_list = []

    for element in numpy_list:
        if isinstance(element, numpy.ndarray):
            element = __convert_to_builtin(element)
        elif numpy.isnan(element):
            element = None
        else:
            element = element.item()

        new_list.append(element)

    return new_list


# ---------------------------------------------------------------------------------------------------------------------------------------- #