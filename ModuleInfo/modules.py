'''
Making module objects using the Classes from module_constructor 
By providing the module name as a string and respective module_data object from modules_data.
'''

from module_constructor_ import *
import modules_data as m

datetime = ModuleC("datetime", m.DATETIME)

collection = ModuleC("collections", m.COLLECTIONS)

schedule = Module("schedule", m.SCHEDULE)

random = Module("random", m.RANDOM)

numpy = Module("numpy", m.NUMPY)

time = Module("time", m.TIME)

pandas = Module("pandas", m.PANDAS)

os = Module("os", m.OS)
