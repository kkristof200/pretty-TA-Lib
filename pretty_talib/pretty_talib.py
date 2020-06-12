# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, List, Dict, Union, Any

# Pip
from jsoncodable import JSONCodable

from talib import abstract
import numpy

# Local
from .enums.function_name import FunctionName

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

__ALL_METHODS_KEY = 'ALL'
ALL = __ALL_METHODS_KEY

# Supports 'ALL' as type
def get_stats(
    data: Dict[str, numpy.ndarray],
    types: Union[List[FunctionName], str] = __ALL_METHODS_KEY,
    timeperiod: int = 30,
    use_builtin_types: bool = False,
    use_objects: bool = False
) -> Optional[Union[Dict[str, Any], object]]:
    """Creates TA data for the selected types of analysises

    Args:
        data (Dict[str, numpy.ndarray]): The data to analyze. Should be provided in the following format:
        {
            'open': numpy.ndarray,
            'high': numpy.ndarray,
            'low': numpy.ndarray,
            'close': numpy.ndarray,
            'volume': numpy.ndarray,
        }

        types ([Union[List[FunctionName], str]]): The analysis types, you want to perform.
                                                  Defaults to ALL.

        timeperiod (int, optional): Time period to calculate analysis with.
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
    if isinstance(types, str):
        if types.upper() == __ALL_METHODS_KEY:
            types = [function_name for function_name in FunctionName]
        else:
            return None

    func_names = [function_name.value for function_name in types]
    res = {}

    for func_name in func_names:
        func = abstract.Function(func_name)

        try:
            _res = func(data, timeperiod=timeperiod)

            if use_builtin_types or use_objects:
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