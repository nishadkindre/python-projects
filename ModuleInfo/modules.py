'''
Making module objects using the Classes from module_constructor 
By providing the module name as a string and respective module_data object from modules_data.
'''

from module_constructor_ import *
import modules_data as m

datetime = ModuleC(name='datetime', data=m.DATETIME_DATA)

collection = ModuleC('collections', m.COLLECTIONS_DATA)

schedule = Module('schedule', m.SCHEDULE_DATA)

random = Module('random', m.RANDOM_DATA)

numpy = Module('numpy', m.NUMPY_DATA)

time = Module('time', m.TIME_DATA)

pandas = Module('pandas', m.PANDAS_DATA)

os = Module('os', m.OS_DATA)

math = Module('math', m.MATH_DATA)
