'''
Making module objects using the Classes from module_constructor 
By providing the module name as a string and respective module_data object from modules_data.
'''

from module_constructor_ import *
from modules_data import \
schedule_data , random_data , numpy_data , time_data , \
pandas_data , os_data , collections_data , datetime_data

datetime = ModuleC("datetime", datetime_data)

collection = ModuleC("collections", collections_data)

schedule = Module("schedule", schedule_data)

random = Module("random", random_data)

numpy = Module("numpy", numpy_data)

time = Module("time", time_data)

pandas = Module("pandas", pandas_data)

os = Module("os", os_data)
