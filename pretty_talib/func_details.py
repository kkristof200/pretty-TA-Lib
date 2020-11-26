details = {
	'cycle_indicators': {
		'HT_DCPERIOD': {
			'ta_name_short': 'HT_DCPERIOD',
			'ta_name_full': 'Hilbert Transform',
			'note': 'The ``HT_DCPERIOD`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'HT_DCPERIOD',
			'args': ['close'],
			'kwargs': {}
		},
		'HT_DCPHASE': {
			'ta_name_short': 'HT_DCPHASE',
			'ta_name_full': 'Hilbert Transform',
			'note': 'The ``HT_DCPHASE`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'HT_DCPHASE',
			'args': ['close'],
			'kwargs': {}
		},
		'HT_PHASOR': {
			'ta_name_short': 'HT_PHASOR',
			'ta_name_full': 'Hilbert Transform',
			'note': 'The ``HT_PHASOR`` function has an unstable period.',
			'returns': ['inphase', 'quadrature'],
			'func_name': 'HT_PHASOR',
			'args': ['close'],
			'kwargs': {}
		},
		'HT_SINE': {
			'ta_name_short': 'HT_SINE',
			'ta_name_full': 'Hilbert Transform',
			'note': 'The ``HT_SINE`` function has an unstable period.',
			'returns': ['sine', 'leadsine'],
			'func_name': 'HT_SINE',
			'args': ['close'],
			'kwargs': {}
		},
		'HT_TRENDMODE': {
			'ta_name_short': 'HT_TRENDMODE',
			'ta_name_full': 'Hilbert Transform',
			'note': None,
			'returns': ['integer'],
			'func_name': 'HT_TRENDMODE',
			'args': ['close'],
			'kwargs': {}
		}
	},
	'ath_operators': {
		'ADD': {
			'ta_name_short': 'ADD',
			'ta_name_full': 'Vector Arithmetic Add',
			'note': None,
			'returns': ['real'],
			'func_name': 'ADD',
			'args': ['high', 'low'],
			'kwargs': {}
		},
		'DIV': {
			'ta_name_short': 'DIV',
			'ta_name_full': 'Vector Arithmetic Div',
			'note': None,
			'returns': ['real'],
			'func_name': 'DIV',
			'args': ['high', 'low'],
			'kwargs': {}
		},
		'MAX': {
			'ta_name_short': 'MAX',
			'ta_name_full': 'Highest value over a specified period',
			'note': None,
			'returns': ['real'],
			'func_name': 'MAX',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MAXINDEX': {
			'ta_name_short': 'MAXINDEX',
			'ta_name_full': 'Index of highest value over a specified period',
			'note': None,
			'returns': ['integer'],
			'func_name': 'MAXINDEX',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MIN': {
			'ta_name_short': 'MIN',
			'ta_name_full': 'Lowest value over a specified period',
			'note': None,
			'returns': ['real'],
			'func_name': 'MIN',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MININDEX': {
			'ta_name_short': 'MININDEX',
			'ta_name_full': 'Index of lowest value over a specified period',
			'note': None,
			'returns': ['integer'],
			'func_name': 'MININDEX',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MINMAX': {
			'ta_name_short': 'MINMAX',
			'ta_name_full': 'Lowest and highest values over a specified period',
			'note': None,
			'returns': ['min', 'max'],
			'func_name': 'MINMAX',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MINMAXINDEX': {
			'ta_name_short': 'MINMAXINDEX',
			'ta_name_full': 'Indexes of lowest and highest values over a specified period',
			'note': None,
			'returns': ['minidx', 'maxidx'],
			'func_name': 'MINMAXINDEX',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MULT': {
			'ta_name_short': 'MULT',
			'ta_name_full': 'Vector Arithmetic Mult',
			'note': None,
			'returns': ['real'],
			'func_name': 'MULT',
			'args': ['high', 'low'],
			'kwargs': {}
		},
		'SUB': {
			'ta_name_short': 'SUB',
			'ta_name_full': 'Vector Arithmetic Substraction',
			'note': None,
			'returns': ['real'],
			'func_name': 'SUB',
			'args': ['high', 'low'],
			'kwargs': {}
		},
		'SUM': {
			'ta_name_short': 'SUM',
			'ta_name_full': 'Summation',
			'note': None,
			'returns': ['real'],
			'func_name': 'SUM',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		}
	},
	'ath_transfor': {
		'ACOS': {
			'ta_name_short': 'ACOS',
			'ta_name_full': 'Vector Trigonometric ACos',
			'note': None,
			'returns': ['real'],
			'func_name': 'ACOS',
			'args': ['close'],
			'kwargs': {}
		},
		'ASIN': {
			'ta_name_short': 'ASIN',
			'ta_name_full': 'Vector Trigonometric ASin',
			'note': None,
			'returns': ['real'],
			'func_name': 'ASIN',
			'args': ['close'],
			'kwargs': {}
		},
		'ATAN': {
			'ta_name_short': 'ATAN',
			'ta_name_full': 'Vector Trigonometric ATan',
			'note': None,
			'returns': ['real'],
			'func_name': 'ATAN',
			'args': ['close'],
			'kwargs': {}
		},
		'CEIL': {
			'ta_name_short': 'CEIL',
			'ta_name_full': 'Vector Ceil',
			'note': None,
			'returns': ['real'],
			'func_name': 'CEIL',
			'args': ['close'],
			'kwargs': {}
		},
		'COS': {
			'ta_name_short': 'COS',
			'ta_name_full': 'Vector Trigonometric Cos',
			'note': None,
			'returns': ['real'],
			'func_name': 'COS',
			'args': ['close'],
			'kwargs': {}
		},
		'COSH': {
			'ta_name_short': 'COSH',
			'ta_name_full': 'Vector Trigonometric Cosh',
			'note': None,
			'returns': ['real'],
			'func_name': 'COSH',
			'args': ['close'],
			'kwargs': {}
		},
		'EXP': {
			'ta_name_short': 'EXP',
			'ta_name_full': 'Vector Arithmetic Exp',
			'note': None,
			'returns': ['real'],
			'func_name': 'EXP',
			'args': ['close'],
			'kwargs': {}
		},
		'FLOOR': {
			'ta_name_short': 'FLOOR',
			'ta_name_full': 'Vector Floor',
			'note': None,
			'returns': ['real'],
			'func_name': 'FLOOR',
			'args': ['close'],
			'kwargs': {}
		},
		'LN': {
			'ta_name_short': 'LN',
			'ta_name_full': 'Vector Log Natural',
			'note': None,
			'returns': ['real'],
			'func_name': 'LN',
			'args': ['close'],
			'kwargs': {}
		},
		'LOG10': {
			'ta_name_short': 'LOG10',
			'ta_name_full': 'Vector Log10',
			'note': None,
			'returns': ['real'],
			'func_name': 'LOG10',
			'args': ['close'],
			'kwargs': {}
		},
		'SIN': {
			'ta_name_short': 'SIN',
			'ta_name_full': 'Vector Trigonometric Sin',
			'note': None,
			'returns': ['real'],
			'func_name': 'SIN',
			'args': ['close'],
			'kwargs': {}
		},
		'SINH': {
			'ta_name_short': 'SINH',
			'ta_name_full': 'Vector Trigonometric Sinh',
			'note': None,
			'returns': ['real'],
			'func_name': 'SINH',
			'args': ['close'],
			'kwargs': {}
		},
		'SQRT': {
			'ta_name_short': 'SQRT',
			'ta_name_full': 'Vector Square Root',
			'note': None,
			'returns': ['real'],
			'func_name': 'SQRT',
			'args': ['close'],
			'kwargs': {}
		},
		'TAN': {
			'ta_name_short': 'TAN',
			'ta_name_full': 'Vector Trigonometric Tan',
			'note': None,
			'returns': ['real'],
			'func_name': 'TAN',
			'args': ['close'],
			'kwargs': {}
		},
		'TANH': {
			'ta_name_short': 'TANH',
			'ta_name_full': 'Vector Trigonometric Tanh',
			'note': None,
			'returns': ['real'],
			'func_name': 'TANH',
			'args': ['close'],
			'kwargs': {}
		}
	},
	'omentum_indicators': {
		'ADX': {
			'ta_name_short': 'ADX',
			'ta_name_full': 'Average Directional Movement Index',
			'note': 'The ``ADX`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'ADX',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'ADXR': {
			'ta_name_short': 'ADXR',
			'ta_name_full': 'Average Directional Movement Index Rating',
			'note': 'The ``ADXR`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'ADXR',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'APO': {
			'ta_name_short': 'APO',
			'ta_name_full': 'Absolute Price Oscillator',
			'note': None,
			'returns': ['real'],
			'func_name': 'APO',
			'args': ['close'],
			'kwargs': {
				'fastperiod': 12,
				'slowperiod': 26,
				'matype': 0
			}
		},
		'AROON': {
			'ta_name_short': 'AROON',
			'ta_name_full': 'Aroon',
			'note': None,
			'returns': ['aroondown', 'aroonup'],
			'func_name': 'AROON',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'AROONOSC': {
			'ta_name_short': 'AROONOSC',
			'ta_name_full': 'Aroon Oscillator',
			'note': None,
			'returns': ['real'],
			'func_name': 'AROONOSC',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'BOP': {
			'ta_name_short': 'BOP',
			'ta_name_full': 'Balance Of Power',
			'note': None,
			'returns': ['real'],
			'func_name': 'BOP',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CCI': {
			'ta_name_short': 'CCI',
			'ta_name_full': 'Commodity Channel Index',
			'note': None,
			'returns': ['real'],
			'func_name': 'CCI',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'CMO': {
			'ta_name_short': 'CMO',
			'ta_name_full': 'Chande Momentum Oscillator',
			'note': 'The ``CMO`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'CMO',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'DX': {
			'ta_name_short': 'DX',
			'ta_name_full': 'Directional Movement Index',
			'note': 'The ``DX`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'DX',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'MACD': {
			'ta_name_short': 'MACD',
			'ta_name_full': 'Moving Average Convergence/Divergence',
			'note': None,
			'returns': ['macd', 'macdsignal', 'macdhist'],
			'func_name': 'MACD',
			'args': ['close'],
			'kwargs': {
				'fastperiod': 12,
				'slowperiod': 26,
				'signalperiod': 9
			}
		},
		'MACDEXT': {
			'ta_name_short': 'MACDEXT',
			'ta_name_full': 'MACD with controllable MA type',
			'note': None,
			'returns': ['macd', 'macdsignal', 'macdhist'],
			'func_name': 'MACDEXT',
			'args': ['close'],
			'kwargs': {
				'fastperiod': 12,
				'fastmatype': 0,
				'slowperiod': 26,
				'slowmatype': 0,
				'signalperiod': 9,
				'signalmatype': 0
			}
		},
		'MACDFIX': {
			'ta_name_short': 'MACDFIX',
			'ta_name_full': 'Moving Average Convergence/Divergence Fix 12/26',
			'note': None,
			'returns': ['macd', 'macdsignal', 'macdhist'],
			'func_name': 'MACDFIX',
			'args': ['close'],
			'kwargs': {
				'signalperiod': 9
			}
		},
		'MFI': {
			'ta_name_short': 'MFI',
			'ta_name_full': 'Money Flow Index',
			'note': 'The ``MFI`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'MFI',
			'args': ['high', 'low', 'close', 'volume'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'MINUS_DI': {
			'ta_name_short': 'MINUS_DI',
			'ta_name_full': 'Minus Directional Indicator',
			'note': 'The ``MINUS_DI`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'MINUS_DI',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'MINUS_DM': {
			'ta_name_short': 'MINUS_DM',
			'ta_name_full': 'Minus Directional Movement',
			'note': 'The ``MINUS_DM`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'MINUS_DM',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'MOM': {
			'ta_name_short': 'MOM',
			'ta_name_full': 'Momentum',
			'note': None,
			'returns': ['real'],
			'func_name': 'MOM',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 10
			}
		},
		'PLUS_DI': {
			'ta_name_short': 'PLUS_DI',
			'ta_name_full': 'Plus Directional Indicator',
			'note': 'The ``PLUS_DI`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'PLUS_DI',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'PLUS_DM': {
			'ta_name_short': 'PLUS_DM',
			'ta_name_full': 'Plus Directional Movement',
			'note': 'The ``PLUS_DM`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'PLUS_DM',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'PPO': {
			'ta_name_short': 'PPO',
			'ta_name_full': 'Percentage Price Oscillator',
			'note': None,
			'returns': ['real'],
			'func_name': 'PPO',
			'args': ['close'],
			'kwargs': {
				'fastperiod': 12,
				'slowperiod': 26,
				'matype': 0
			}
		},
		'ROC': {
			'ta_name_short': 'ROC',
			'ta_name_full': 'Rate of change : ((price/prevPrice)',
			'note': None,
			'returns': ['real'],
			'func_name': 'ROC',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 10
			}
		},
		'ROCP': {
			'ta_name_short': 'ROCP',
			'ta_name_full': 'Rate of change Percentage: (price',
			'note': None,
			'returns': ['real'],
			'func_name': 'ROCP',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 10
			}
		},
		'ROCR': {
			'ta_name_short': 'ROCR',
			'ta_name_full': 'Rate of change ratio: (price/prevPrice)',
			'note': None,
			'returns': ['real'],
			'func_name': 'ROCR',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 10
			}
		},
		'ROCR100': {
			'ta_name_short': 'ROCR100',
			'ta_name_full': 'Rate of change ratio 100 scale: (price/prevPrice)*100',
			'note': None,
			'returns': ['real'],
			'func_name': 'ROCR100',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 10
			}
		},
		'RSI': {
			'ta_name_short': 'RSI',
			'ta_name_full': 'Relative Strength Index',
			'note': 'The ``RSI`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'RSI',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'STOCH': {
			'ta_name_short': 'STOCH',
			'ta_name_full': 'Stochastic',
			'note': None,
			'returns': ['slowk', 'slowd'],
			'func_name': 'STOCH',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'fastk_period': 5,
				'slowk_period': 3,
				'slowk_matype': 0,
				'slowd_period': 3,
				'slowd_matype': 0
			}
		},
		'STOCHF': {
			'ta_name_short': 'STOCHF',
			'ta_name_full': 'Stochastic Fast',
			'note': None,
			'returns': ['fastk', 'fastd'],
			'func_name': 'STOCHF',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'fastk_period': 5,
				'fastd_period': 3,
				'fastd_matype': 0
			}
		},
		'STOCHRSI': {
			'ta_name_short': 'STOCHRSI',
			'ta_name_full': 'Stochastic Relative Strength Index',
			'note': 'The ``STOCHRSI`` function has an unstable period.',
			'returns': ['fastk', 'fastd'],
			'func_name': 'STOCHRSI',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14,
				'fastk_period': 5,
				'fastd_period': 3,
				'fastd_matype': 0
			}
		},
		'TRIX': {
			'ta_name_short': 'TRIX',
			'ta_name_full': '1',
			'note': None,
			'returns': ['real'],
			'func_name': 'TRIX',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'ULTOSC': {
			'ta_name_short': 'ULTOSC',
			'ta_name_full': 'Ultimate Oscillator',
			'note': None,
			'returns': ['real'],
			'func_name': 'ULTOSC',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod1': 7,
				'timeperiod2': 14,
				'timeperiod3': 28
			}
		},
		'WILLR': {
			'ta_name_short': 'WILLR',
			'ta_name_full': "Williams' %R",
			'note': None,
			'returns': ['real'],
			'func_name': 'WILLR',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		}
	},
	'overlap_studies': {
		'BBANDS': {
			'ta_name_short': 'BBANDS',
			'ta_name_full': 'Bollinger Bands',
			'note': None,
			'returns': ['upperband', 'middleband', 'lowerband'],
			'func_name': 'BBANDS',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 5,
				'nbdevup': 2,
				'nbdevdn': 2,
				'matype': 0
			}
		},
		'DEMA': {
			'ta_name_short': 'DEMA',
			'ta_name_full': 'Double Exponential Moving Average',
			'note': None,
			'returns': ['real'],
			'func_name': 'DEMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'EMA': {
			'ta_name_short': 'EMA',
			'ta_name_full': 'Exponential Moving Average',
			'note': 'The ``EMA`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'EMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'HT_TRENDLINE': {
			'ta_name_short': 'HT_TRENDLINE',
			'ta_name_full': 'Hilbert Transform',
			'note': 'The ``HT_TRENDLINE`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'HT_TRENDLINE',
			'args': ['close'],
			'kwargs': {}
		},
		'KAMA': {
			'ta_name_short': 'KAMA',
			'ta_name_full': 'Kaufman Adaptive Moving Average',
			'note': 'The ``KAMA`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'KAMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'MA': {
			'ta_name_short': 'MA',
			'ta_name_full': 'Moving average',
			'note': None,
			'returns': ['real'],
			'func_name': 'MA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30,
				'matype': 0
			}
		},
		'MAMA': {
			'ta_name_short': 'MAMA',
			'ta_name_full': 'MESA Adaptive Moving Average',
			'note': 'The ``MAMA`` function has an unstable period.',
			'returns': ['mama', 'fama'],
			'func_name': 'MAMA',
			'args': ['close'],
			'kwargs': {
				'fastlimit': 0,
				'slowlimit': 0
			}
		},
		'MAVP': {
			'ta_name_short': 'MAVP',
			'ta_name_full': 'Moving average with variable period',
			'note': None,
			'returns': ['real'],
			'func_name': 'MAVP',
			'args': ['close', 'periods'],
			'kwargs': {
				'minperiod': 2,
				'maxperiod': 30,
				'matype': 0
			}
		},
		'MIDPOINT': {
			'ta_name_short': 'MIDPOINT',
			'ta_name_full': 'MidPoint over period',
			'note': None,
			'returns': ['real'],
			'func_name': 'MIDPOINT',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'MIDPRICE': {
			'ta_name_short': 'MIDPRICE',
			'ta_name_full': 'Midpoint Price over period',
			'note': None,
			'returns': ['real'],
			'func_name': 'MIDPRICE',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'SAR': {
			'ta_name_short': 'SAR',
			'ta_name_full': 'Parabolic SAR',
			'note': None,
			'returns': ['real'],
			'func_name': 'SAR',
			'args': ['high', 'low'],
			'kwargs': {
				'acceleration': 0,
				'maximum': 0
			}
		},
		'SAREXT': {
			'ta_name_short': 'SAREXT',
			'ta_name_full': 'Parabolic SAR',
			'note': None,
			'returns': ['real'],
			'func_name': 'SAREXT',
			'args': ['high', 'low'],
			'kwargs': {
				'startvalue': 0,
				'offsetonreverse': 0,
				'accelerationinitlong': 0,
				'accelerationlong': 0,
				'accelerationmaxlong': 0,
				'accelerationinitshort': 0,
				'accelerationshort': 0,
				'accelerationmaxshort': 0
			}
		},
		'SMA': {
			'ta_name_short': 'SMA',
			'ta_name_full': 'Simple Moving Average',
			'note': None,
			'returns': ['real'],
			'func_name': 'SMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'T3': {
			'ta_name_short': 'T3',
			'ta_name_full': 'Triple Exponential Moving Average (T3)',
			'note': 'The ``T3`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'T3',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 5,
				'vfactor': 0
			}
		},
		'TEMA': {
			'ta_name_short': 'TEMA',
			'ta_name_full': 'Triple Exponential Moving Average',
			'note': None,
			'returns': ['real'],
			'func_name': 'TEMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'TRIMA': {
			'ta_name_short': 'TRIMA',
			'ta_name_full': 'Triangular Moving Average',
			'note': None,
			'returns': ['real'],
			'func_name': 'TRIMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'WMA': {
			'ta_name_short': 'WMA',
			'ta_name_full': 'Weighted Moving Average',
			'note': None,
			'returns': ['real'],
			'func_name': 'WMA',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 30
			}
		}
	},
	'pattern_recognition': {
		'CDL2CROWS': {
			'ta_name_short': 'CDL2CROWS',
			'ta_name_full': 'Two Crows',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL2CROWS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDL3BLACKCROWS': {
			'ta_name_short': 'CDL3BLACKCROWS',
			'ta_name_full': 'Three Black Crows',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL3BLACKCROWS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDL3INSIDE': {
			'ta_name_short': 'CDL3INSIDE',
			'ta_name_full': 'Three Inside Up/Down',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL3INSIDE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDL3LINESTRIKE': {
			'ta_name_short': 'CDL3LINESTRIKE',
			'ta_name_full': 'Three',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL3LINESTRIKE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDL3OUTSIDE': {
			'ta_name_short': 'CDL3OUTSIDE',
			'ta_name_full': 'Three Outside Up/Down',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL3OUTSIDE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDL3STARSINSOUTH': {
			'ta_name_short': 'CDL3STARSINSOUTH',
			'ta_name_full': 'Three Stars In The South',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL3STARSINSOUTH',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDL3WHITESOLDIERS': {
			'ta_name_short': 'CDL3WHITESOLDIERS',
			'ta_name_full': 'Three Advancing White Soldiers',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDL3WHITESOLDIERS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLABANDONEDBABY': {
			'ta_name_short': 'CDLABANDONEDBABY',
			'ta_name_full': 'Abandoned Baby',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLABANDONEDBABY',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLADVANCEBLOCK': {
			'ta_name_short': 'CDLADVANCEBLOCK',
			'ta_name_full': 'Advance Block',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLADVANCEBLOCK',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLBELTHOLD': {
			'ta_name_short': 'CDLBELTHOLD',
			'ta_name_full': 'Belt',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLBELTHOLD',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLBREAKAWAY': {
			'ta_name_short': 'CDLBREAKAWAY',
			'ta_name_full': 'Breakaway',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLBREAKAWAY',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLCLOSINGMARUBOZU': {
			'ta_name_short': 'CDLCLOSINGMARUBOZU',
			'ta_name_full': 'Closing Marubozu',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLCLOSINGMARUBOZU',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLCONCEALBABYSWALL': {
			'ta_name_short': 'CDLCONCEALBABYSWALL',
			'ta_name_full': 'Concealing Baby Swallow',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLCONCEALBABYSWALL',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLCOUNTERATTACK': {
			'ta_name_short': 'CDLCOUNTERATTACK',
			'ta_name_full': 'Counterattack',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLCOUNTERATTACK',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLDARKCLOUDCOVER': {
			'ta_name_short': 'CDLDARKCLOUDCOVER',
			'ta_name_full': 'Dark Cloud Cover',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLDARKCLOUDCOVER',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLDOJI': {
			'ta_name_short': 'CDLDOJI',
			'ta_name_full': 'Doji',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLDOJI',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLDOJISTAR': {
			'ta_name_short': 'CDLDOJISTAR',
			'ta_name_full': 'Doji Star',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLDOJISTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLDRAGONFLYDOJI': {
			'ta_name_short': 'CDLDRAGONFLYDOJI',
			'ta_name_full': 'Dragonfly Doji',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLDRAGONFLYDOJI',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLENGULFING': {
			'ta_name_short': 'CDLENGULFING',
			'ta_name_full': 'Engulfing Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLENGULFING',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLEVENINGDOJISTAR': {
			'ta_name_short': 'CDLEVENINGDOJISTAR',
			'ta_name_full': 'Evening Doji Star',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLEVENINGDOJISTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLEVENINGSTAR': {
			'ta_name_short': 'CDLEVENINGSTAR',
			'ta_name_full': 'Evening Star',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLEVENINGSTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLGAPSIDESIDEWHITE': {
			'ta_name_short': 'CDLGAPSIDESIDEWHITE',
			'ta_name_full': 'Up/Down',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLGAPSIDESIDEWHITE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLGRAVESTONEDOJI': {
			'ta_name_short': 'CDLGRAVESTONEDOJI',
			'ta_name_full': 'Gravestone Doji',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLGRAVESTONEDOJI',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHAMMER': {
			'ta_name_short': 'CDLHAMMER',
			'ta_name_full': 'Hammer',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHAMMER',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHANGINGMAN': {
			'ta_name_short': 'CDLHANGINGMAN',
			'ta_name_full': 'Hanging Man',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHANGINGMAN',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHARAMI': {
			'ta_name_short': 'CDLHARAMI',
			'ta_name_full': 'Harami Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHARAMI',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHARAMICROSS': {
			'ta_name_short': 'CDLHARAMICROSS',
			'ta_name_full': 'Harami Cross Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHARAMICROSS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHIGHWAVE': {
			'ta_name_short': 'CDLHIGHWAVE',
			'ta_name_full': 'High',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHIGHWAVE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHIKKAKE': {
			'ta_name_short': 'CDLHIKKAKE',
			'ta_name_full': 'Hikkake Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHIKKAKE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHIKKAKEMOD': {
			'ta_name_short': 'CDLHIKKAKEMOD',
			'ta_name_full': 'Modified Hikkake Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHIKKAKEMOD',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLHOMINGPIGEON': {
			'ta_name_short': 'CDLHOMINGPIGEON',
			'ta_name_full': 'Homing Pigeon',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLHOMINGPIGEON',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLIDENTICAL3CROWS': {
			'ta_name_short': 'CDLIDENTICAL3CROWS',
			'ta_name_full': 'Identical Three Crows',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLIDENTICAL3CROWS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLINNECK': {
			'ta_name_short': 'CDLINNECK',
			'ta_name_full': 'In',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLINNECK',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLINVERTEDHAMMER': {
			'ta_name_short': 'CDLINVERTEDHAMMER',
			'ta_name_full': 'Inverted Hammer',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLINVERTEDHAMMER',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLKICKING': {
			'ta_name_short': 'CDLKICKING',
			'ta_name_full': 'Kicking',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLKICKING',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLKICKINGBYLENGTH': {
			'ta_name_short': 'CDLKICKINGBYLENGTH',
			'ta_name_full': 'Kicking',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLKICKINGBYLENGTH',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLLADDERBOTTOM': {
			'ta_name_short': 'CDLLADDERBOTTOM',
			'ta_name_full': 'Ladder Bottom',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLLADDERBOTTOM',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLLONGLEGGEDDOJI': {
			'ta_name_short': 'CDLLONGLEGGEDDOJI',
			'ta_name_full': 'Long Legged Doji',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLLONGLEGGEDDOJI',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLLONGLINE': {
			'ta_name_short': 'CDLLONGLINE',
			'ta_name_full': 'Long Line Candle',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLLONGLINE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLMARUBOZU': {
			'ta_name_short': 'CDLMARUBOZU',
			'ta_name_full': 'Marubozu',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLMARUBOZU',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLMATCHINGLOW': {
			'ta_name_short': 'CDLMATCHINGLOW',
			'ta_name_full': 'Matching Low',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLMATCHINGLOW',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLMATHOLD': {
			'ta_name_short': 'CDLMATHOLD',
			'ta_name_full': 'Mat Hold',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLMATHOLD',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLMORNINGDOJISTAR': {
			'ta_name_short': 'CDLMORNINGDOJISTAR',
			'ta_name_full': 'Morning Doji Star',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLMORNINGDOJISTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLMORNINGSTAR': {
			'ta_name_short': 'CDLMORNINGSTAR',
			'ta_name_full': 'Morning Star',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLMORNINGSTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {
				'penetration': 0
			}
		},
		'CDLONNECK': {
			'ta_name_short': 'CDLONNECK',
			'ta_name_full': 'On',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLONNECK',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLPIERCING': {
			'ta_name_short': 'CDLPIERCING',
			'ta_name_full': 'Piercing Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLPIERCING',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLRICKSHAWMAN': {
			'ta_name_short': 'CDLRICKSHAWMAN',
			'ta_name_full': 'Rickshaw Man',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLRICKSHAWMAN',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLRISEFALL3METHODS': {
			'ta_name_short': 'CDLRISEFALL3METHODS',
			'ta_name_full': 'Rising/Falling Three Methods',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLRISEFALL3METHODS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLSEPARATINGLINES': {
			'ta_name_short': 'CDLSEPARATINGLINES',
			'ta_name_full': 'Separating Lines',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLSEPARATINGLINES',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLSHOOTINGSTAR': {
			'ta_name_short': 'CDLSHOOTINGSTAR',
			'ta_name_full': 'Shooting Star',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLSHOOTINGSTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLSHORTLINE': {
			'ta_name_short': 'CDLSHORTLINE',
			'ta_name_full': 'Short Line Candle',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLSHORTLINE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLSPINNINGTOP': {
			'ta_name_short': 'CDLSPINNINGTOP',
			'ta_name_full': 'Spinning Top',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLSPINNINGTOP',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLSTALLEDPATTERN': {
			'ta_name_short': 'CDLSTALLEDPATTERN',
			'ta_name_full': 'Stalled Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLSTALLEDPATTERN',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLSTICKSANDWICH': {
			'ta_name_short': 'CDLSTICKSANDWICH',
			'ta_name_full': 'Stick Sandwich',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLSTICKSANDWICH',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLTAKURI': {
			'ta_name_short': 'CDLTAKURI',
			'ta_name_full': 'Takuri (Dragonfly Doji with very long lower shadow)',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLTAKURI',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLTASUKIGAP': {
			'ta_name_short': 'CDLTASUKIGAP',
			'ta_name_full': 'Tasuki Gap',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLTASUKIGAP',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLTHRUSTING': {
			'ta_name_short': 'CDLTHRUSTING',
			'ta_name_full': 'Thrusting Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLTHRUSTING',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLTRISTAR': {
			'ta_name_short': 'CDLTRISTAR',
			'ta_name_full': 'Tristar Pattern',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLTRISTAR',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLUNIQUE3RIVER': {
			'ta_name_short': 'CDLUNIQUE3RIVER',
			'ta_name_full': 'Unique 3 River',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLUNIQUE3RIVER',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLUPSIDEGAP2CROWS': {
			'ta_name_short': 'CDLUPSIDEGAP2CROWS',
			'ta_name_full': 'Upside Gap Two Crows',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLUPSIDEGAP2CROWS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'CDLXSIDEGAP3METHODS': {
			'ta_name_short': 'CDLXSIDEGAP3METHODS',
			'ta_name_full': 'Upside/Downside Gap Three Methods',
			'note': None,
			'returns': ['integer'],
			'func_name': 'CDLXSIDEGAP3METHODS',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		}
	},
	'price_transfor': {
		'AVGPRICE': {
			'ta_name_short': 'AVGPRICE',
			'ta_name_full': 'Average Price',
			'note': None,
			'returns': ['real'],
			'func_name': 'AVGPRICE',
			'args': ['open', 'high', 'low', 'close'],
			'kwargs': {}
		},
		'MEDPRICE': {
			'ta_name_short': 'MEDPRICE',
			'ta_name_full': 'Median Price',
			'note': None,
			'returns': ['real'],
			'func_name': 'MEDPRICE',
			'args': ['high', 'low'],
			'kwargs': {}
		},
		'TYPPRICE': {
			'ta_name_short': 'TYPPRICE',
			'ta_name_full': 'Typical Price',
			'note': None,
			'returns': ['real'],
			'func_name': 'TYPPRICE',
			'args': ['high', 'low', 'close'],
			'kwargs': {}
		},
		'WCLPRICE': {
			'ta_name_short': 'WCLPRICE',
			'ta_name_full': 'Weighted Close Price',
			'note': None,
			'returns': ['real'],
			'func_name': 'WCLPRICE',
			'args': ['high', 'low', 'close'],
			'kwargs': {}
		}
	},
	'statistic_functions': {
		'BETA': {
			'ta_name_short': 'BETA',
			'ta_name_full': 'Beta',
			'note': None,
			'returns': ['real'],
			'func_name': 'BETA',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 5
			}
		},
		'CORREL': {
			'ta_name_short': 'CORREL',
			'ta_name_full': "Pearson's Correlation Coefficient (r)",
			'note': None,
			'returns': ['real'],
			'func_name': 'CORREL',
			'args': ['high', 'low'],
			'kwargs': {
				'timeperiod': 30
			}
		},
		'LINEARREG': {
			'ta_name_short': 'LINEARREG',
			'ta_name_full': 'Linear Regression',
			'note': None,
			'returns': ['real'],
			'func_name': 'LINEARREG',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'LINEARREG_ANGLE': {
			'ta_name_short': 'LINEARREG_ANGLE',
			'ta_name_full': 'Linear Regression Angle',
			'note': None,
			'returns': ['real'],
			'func_name': 'LINEARREG_ANGLE',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'LINEARREG_INTERCEPT': {
			'ta_name_short': 'LINEARREG_INTERCEPT',
			'ta_name_full': 'Linear Regression Intercept',
			'note': None,
			'returns': ['real'],
			'func_name': 'LINEARREG_INTERCEPT',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'LINEARREG_SLOPE': {
			'ta_name_short': 'LINEARREG_SLOPE',
			'ta_name_full': 'Linear Regression Slope',
			'note': None,
			'returns': ['real'],
			'func_name': 'LINEARREG_SLOPE',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'STDDEV': {
			'ta_name_short': 'STDDEV',
			'ta_name_full': 'Standard Deviation',
			'note': None,
			'returns': ['real'],
			'func_name': 'STDDEV',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 5,
				'nbdev': 1
			}
		},
		'TSF': {
			'ta_name_short': 'TSF',
			'ta_name_full': 'Time Series Forecast',
			'note': None,
			'returns': ['real'],
			'func_name': 'TSF',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'VAR': {
			'ta_name_short': 'VAR',
			'ta_name_full': 'Variance',
			'note': None,
			'returns': ['real'],
			'func_name': 'VAR',
			'args': ['close'],
			'kwargs': {
				'timeperiod': 5,
				'nbdev': 1
			}
		}
	},
	'volatility_indicators': {
		'ATR': {
			'ta_name_short': 'ATR',
			'ta_name_full': 'Average True Range',
			'note': 'The ``ATR`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'ATR',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'NATR': {
			'ta_name_short': 'NATR',
			'ta_name_full': 'Normalized Average True Range',
			'note': 'The ``NATR`` function has an unstable period.',
			'returns': ['real'],
			'func_name': 'NATR',
			'args': ['high', 'low', 'close'],
			'kwargs': {
				'timeperiod': 14
			}
		},
		'TRANGE': {
			'ta_name_short': 'TRANGE',
			'ta_name_full': 'True Range',
			'note': None,
			'returns': ['real'],
			'func_name': 'TRANGE',
			'args': ['high', 'low', 'close'],
			'kwargs': {}
		}
	},
	'volume_indicators': {
		'AD': {
			'ta_name_short': 'AD',
			'ta_name_full': 'Chaikin A/D Line',
			'note': None,
			'returns': ['real'],
			'func_name': 'AD',
			'args': ['high', 'low', 'close', 'volume'],
			'kwargs': {}
		},
		'ADOSC': {
			'ta_name_short': 'ADOSC',
			'ta_name_full': 'Chaikin A/D Oscillator',
			'note': None,
			'returns': ['real'],
			'func_name': 'ADOSC',
			'args': ['high', 'low', 'close', 'volume'],
			'kwargs': {
				'fastperiod': 3,
				'slowperiod': 10
			}
		},
		'OBV': {
			'ta_name_short': 'OBV',
			'ta_name_full': 'On Balance Volume',
			'note': None,
			'returns': ['real'],
			'func_name': 'OBV',
			'args': ['close', 'volume'],
			'kwargs': {}
		}
	}
}