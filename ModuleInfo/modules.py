'''
Making module objects using the Classes from module_constructor by providing the module name as a string and respective module_data object from modules_data.
'''

from module_constructor import *

from modules_data import schedule_data , random_data , numpy_data , time_data , pandas_data , os_data , collections_data , datetime_data

datetime = Module("datetime" , datetime_data)

collection = Module("collections" , collections_data)

schedule = Module_("schedule" , schedule_data)

random = Module_("random" , random_data)

numpy = Module_("numpy" , numpy_data)

time = Module_("time" , time_data)

pandas = Module_("pandas" , pandas_data)

os = Module_("os" , os_data)
