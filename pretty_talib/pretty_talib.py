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
from .returns import returns

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
    map_results: bool = False
) -> Optional[Union[Dict[FunctionName, Union[List[numpy.ndarray], numpy.ndarray, pandas.DataFrame, Dict[str, numpy.ndarray]]], object]]:
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

        map_results (bool, optional): maps the result for each function.
                                      For example for 'MACD' the return is a list with 3 numpy.ndarrays
                                      This converts it to a dict with 1 ndarray for each key so it becomes:
                                      {
                                          'macd': numpy.ndarray,
                                          'macdsignal': numpy.ndarray,
                                          'macdhist': numpy.ndarray
                                      }

        IMPORTANT NOTE:
            - THE TYPE OF 'data' AND THE VALUES OF 'use_builtin_types' AND 'use_objects' HIGHLY AFFECTS EFFICIENCY
              SEE BENCHMARK BELOW (Ran 250 times)

            --------------------------------------------------------------------------------------------------
            | rank |                                setup                               |  duration  |  perc |
            --------------------------------------------------------------------------------------------------
            |    1 | data: Dict,             use_builtin_types=False, use_objects=False | 0.00593799 |       |
            |    2 | data: Dict,             use_builtin_types=True,  use_objects=False | 0.03189588 | 5.37x | -> ~5.4x slower
            |    3 | data: Dict,             use_builtin_types=True,  use_objects=True  | 0.03512796 | 5.91x | -> ~5.9x slower
            |    4 | data: pandas.DataFrame, use_builtin_types=False, use_objects=False | 0.03626336 | 6.10x | -> ~6.1x slower
            --------------------------------------------------------------------------------------------------

    Returns:
        Optional[Union[Dict[FunctionName, Union[List[numpy.ndarray], numpy.ndarray, pandas.DataFrame, Dict[str, numpy.ndarray]]], object]]: Returns dictionary, pandas.DataFrame or objects, based on the provided values for 'use_builtin_types', 'use_objects' and 'map_results'
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
        func_name = func_name_enum.value if type(func_name_enum) == FunctionName else str(func_name_enum)
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

            if map_results:
                __res = {}
                _returns = returns[func_name]

                if isinstance(_res, numpy.ndarray):
                    __res[_returns[0]] = _res
                else:
                    i = 0

                    for sub_res in _res:
                        __res[_returns[i]] = sub_res
                        i += 1

                _res = __res

            res[func_name if use_objects else func_name_enum] = _res
        except Exception as e:
            print(func_name, e)

    return res if not use_objects else JSONCodable.from_json(res)

# def get_stepped_stats(
#     data: Dict[str, numpy.ndarray],
#     functions: Dict[Union[FunctionName, str], Tuple[Optional[Tuple], Optional[Dict[str, Any]]]] = {__ALL_METHODS_KEY: (None, None)},
#     timeperiod: Optional[int] = None,
#     map_results: bool = False
# ) -> Optional[Dict[FunctionName, Union[List[numpy.ndarray], numpy.ndarray, pandas.DataFrame]], object]]:

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