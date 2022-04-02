'''
Contains module data 
Making individual module objects to include their respective data used for making module objects from the respective classes from module_constructor.
'''

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR TIME MODULE :
import time
time_methods = tuple(dir(time))

from time import _STRUCT_TM_ITEMS as y
from time import *
time_methods_info = (y.__doc__, time.__doc__.__doc__, __loader__.__doc__, __name__.__doc__, __package__.__doc__, __spec__.__doc__, altzone.__doc__, asctime.__doc__, ctime.__doc__, daylight.__doc__, get_clock_info.__doc__, gmtime.__doc__, localtime.__doc__, mktime.__doc__, monotonic.__doc__, monotonic_ns.__doc__, perf_counter.__doc__, perf_counter_ns.__doc__, process_time.__doc__, process_time_ns.__doc__, sleep.__doc__, strftime.__doc__, strptime.__doc__, struct_time.__doc__, thread_time.__doc__, thread_time_ns.__doc__, time.__doc__, time_ns.__doc__, timezone.__doc__, tzname.__doc__)

a = zip(time_methods , time_methods_info)
time_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR NUMPY MODULE 
import numpy
numpy_methods = tuple(dir(numpy))

numpy_methods_info = (numpy.ALLOW_THREADS.__doc__,numpy.AxisError.__doc__,numpy.BUFSIZE.__doc__,numpy.CLIP.__doc__,numpy.ComplexWarning.__doc__,numpy.DataSource.__doc__,numpy.ERR_CALL.__doc__,numpy.ERR_DEFAULT.__doc__,numpy.ERR_IGNORE.__doc__,numpy.ERR_LOG.__doc__,numpy.ERR_PRINT.__doc__,numpy.ERR_RAISE.__doc__,numpy.ERR_WARN.__doc__,numpy.FLOATING_POINT_SUPPORT.__doc__,numpy.FPE_DIVIDEBYZERO.__doc__,numpy.FPE_INVALID.__doc__,numpy.FPE_OVERFLOW.__doc__,numpy.FPE_UNDERFLOW.__doc__,numpy.False_.__doc__,numpy.Inf.__doc__,numpy.Infinity.__doc__,numpy.MAXDIMS.__doc__,numpy.MAY_SHARE_BOUNDS.__doc__,numpy.MAY_SHARE_EXACT.__doc__,numpy.ModuleDeprecationWarning.__doc__,numpy.NAN.__doc__,numpy.NINF.__doc__,numpy.NZERO.__doc__,numpy.NaN.__doc__,numpy.PINF.__doc__,numpy.PZERO.__doc__,numpy.RAISE.__doc__,numpy.RankWarning.__doc__,numpy.SHIFT_DIVIDEBYZERO.__doc__,numpy.SHIFT_INVALID.__doc__,numpy.SHIFT_OVERFLOW.__doc__,numpy.SHIFT_UNDERFLOW.__doc__,numpy.ScalarType.__doc__,numpy.Tester.__doc__,numpy.TooHardError.__doc__,numpy.True_.__doc__,numpy.UFUNC_BUFSIZE_DEFAULT.__doc__,numpy.UFUNC_PYVALS_NAME.__doc__,numpy.VisibleDeprecationWarning.__doc__,numpy.WRAP.__doc__,numpy._CopyMode.__doc__,numpy._NoValue.__doc__,numpy._UFUNC_API.__doc__,None,numpy.__all__.__doc__,numpy.__builtins__.__doc__,numpy.__cached__.__doc__,numpy.__config__.__doc__,numpy.__deprecated_attrs__.__doc__,numpy.__dir__.__doc__,numpy.__doc__.__doc__,numpy.__expired_functions__.__doc__,numpy.__file__.__doc__,numpy.__getattr__.__doc__,numpy.__git_version__.__doc__,numpy.__loader__.__doc__,numpy.__name__.__doc__,numpy.__package__.__doc__,numpy.__path__.__doc__,numpy.__spec__.__doc__,numpy.__version__.__doc__,numpy._add_newdoc_ufunc.__doc__,numpy._distributor_init.__doc__,numpy._financial_names.__doc__,numpy._from_dlpack.__doc__,numpy._globals.__doc__,numpy._mat.__doc__,numpy._pytesttester.__doc__,numpy._version.__doc__,numpy.abs.__doc__,numpy.absolute.__doc__,numpy.add.__doc__,numpy.add_docstring.__doc__,numpy.add_newdoc.__doc__,numpy.add_newdoc_ufunc.__doc__,numpy.alen.__doc__,numpy.all.__doc__,numpy.allclose.__doc__,numpy.alltrue.__doc__,numpy.amax.__doc__,numpy.amin.__doc__,numpy.angle.__doc__,numpy.any.__doc__,numpy.append.__doc__,numpy.apply_along_axis.__doc__,numpy.apply_over_axes.__doc__,numpy.arange.__doc__,numpy.arccos.__doc__,numpy.arccosh.__doc__,numpy.arcsin.__doc__,numpy.arcsinh.__doc__,numpy.arctan.__doc__,numpy.arctan2.__doc__,numpy.arctanh.__doc__,numpy.argmax.__doc__,numpy.argmin.__doc__,numpy.argpartition.__doc__,numpy.argsort.__doc__,numpy.argwhere.__doc__,numpy.around.__doc__,numpy.array.__doc__,numpy.array2string.__doc__,numpy.array_equal.__doc__,numpy.array_equiv.__doc__,numpy.array_repr.__doc__,numpy.array_split.__doc__,numpy.array_str.__doc__,numpy.asanyarray.__doc__,numpy.asarray.__doc__,numpy.asarray_chkfinite.__doc__,numpy.ascontiguousarray.__doc__,numpy.asfarray.__doc__,numpy.asfortranarray.__doc__,numpy.asmatrix.__doc__,numpy.asscalar.__doc__,numpy.atleast_1d.__doc__,numpy.atleast_2d.__doc__,numpy.atleast_3d.__doc__,numpy.average.__doc__,numpy.bartlett.__doc__,numpy.base_repr.__doc__,numpy.binary_repr.__doc__,numpy.bincount.__doc__,numpy.bitwise_and.__doc__,numpy.bitwise_not.__doc__,numpy.bitwise_or.__doc__,numpy.bitwise_xor.__doc__,numpy.blackman.__doc__,numpy.block.__doc__,numpy.bmat.__doc__,numpy.bool8.__doc__,numpy.bool_.__doc__,numpy.broadcast.__doc__,numpy.broadcast_arrays.__doc__,numpy.broadcast_shapes.__doc__,numpy.broadcast_to.__doc__,numpy.busday_count.__doc__,numpy.busday_offset.__doc__,numpy.busdaycalendar.__doc__,numpy.byte.__doc__,numpy.byte_bounds.__doc__,numpy.bytes0.__doc__,numpy.bytes_.__doc__,numpy.c_.__doc__,numpy.can_cast.__doc__,numpy.cast.__doc__,numpy.cbrt.__doc__,numpy.cdouble.__doc__,numpy.ceil.__doc__,numpy.cfloat.__doc__,numpy.char.__doc__,numpy.character.__doc__,numpy.chararray.__doc__,numpy.choose.__doc__,numpy.clip.__doc__,numpy.clongdouble.__doc__,numpy.clongfloat.__doc__,numpy.column_stack.__doc__,numpy.common_type.__doc__,numpy.compare_chararrays.__doc__,numpy.compat.__doc__,numpy.complex128.__doc__,numpy.complex64.__doc__,numpy.complex_.__doc__,numpy.complexfloating.__doc__,numpy.compress.__doc__,numpy.concatenate.__doc__,numpy.conj.__doc__,numpy.conjugate.__doc__,numpy.convolve.__doc__,numpy.copy.__doc__,numpy.copysign.__doc__,numpy.copyto.__doc__,numpy.core.__doc__,numpy.corrcoef.__doc__,numpy.correlate.__doc__,numpy.cos.__doc__,numpy.cosh.__doc__,numpy.count_nonzero.__doc__,numpy.cov.__doc__,numpy.cross.__doc__,numpy.csingle.__doc__,numpy.ctypeslib.__doc__,numpy.cumprod.__doc__,numpy.cumproduct.__doc__,numpy.cumsum.__doc__,numpy.datetime64.__doc__,numpy.datetime_as_string.__doc__,numpy.datetime_data.__doc__,numpy.deg2rad.__doc__,numpy.degrees.__doc__,numpy.delete.__doc__,numpy.deprecate.__doc__,numpy.deprecate_with_doc.__doc__,numpy.diag.__doc__,numpy.diag_indices.__doc__,numpy.diag_indices_from.__doc__,numpy.diagflat.__doc__,numpy.diagonal.__doc__,numpy.diff.__doc__,numpy.digitize.__doc__,numpy.disp.__doc__,numpy.divide.__doc__,numpy.divmod.__doc__,numpy.dot.__doc__,numpy.double.__doc__,numpy.dsplit.__doc__,numpy.dstack.__doc__,numpy.dtype.__doc__,numpy.e.__doc__,numpy.ediff1d.__doc__,numpy.einsum.__doc__,numpy.einsum_path.__doc__,numpy.emath.__doc__,numpy.empty.__doc__,numpy.empty_like.__doc__,numpy.equal.__doc__,numpy.errstate.__doc__,numpy.euler_gamma.__doc__,numpy.exp.__doc__,numpy.exp2.__doc__,numpy.expand_dims.__doc__,numpy.expm1.__doc__,numpy.extract.__doc__,numpy.eye.__doc__,numpy.fabs.__doc__,numpy.fastCopyAndTranspose.__doc__,numpy.fft.__doc__,numpy.fill_diagonal.__doc__,numpy.find_common_type.__doc__,numpy.finfo.__doc__,numpy.fix.__doc__,numpy.flatiter.__doc__,numpy.flatnonzero.__doc__,numpy.flexible.__doc__,numpy.flip.__doc__,numpy.fliplr.__doc__,numpy.flipud.__doc__,numpy.float16.__doc__,numpy.float32.__doc__,numpy.float64.__doc__,numpy.float_.__doc__,numpy.float_power.__doc__,numpy.floating.__doc__,numpy.floor.__doc__,numpy.floor_divide.__doc__,numpy.fmax.__doc__,numpy.fmin.__doc__,numpy.fmod.__doc__,numpy.format_float_positional.__doc__,numpy.format_float_scientific.__doc__,numpy.format_parser.__doc__,numpy.frexp.__doc__,numpy.frombuffer.__doc__,numpy.fromfile.__doc__,numpy.fromfunction.__doc__,numpy.fromiter.__doc__,numpy.frompyfunc.__doc__,numpy.fromregex.__doc__,numpy.fromstring.__doc__,numpy.full.__doc__,numpy.full_like.__doc__,numpy.gcd.__doc__,numpy.generic.__doc__,numpy.genfromtxt.__doc__,numpy.geomspace.__doc__,numpy.get_array_wrap.__doc__,numpy.get_include.__doc__,numpy.get_printoptions.__doc__,numpy.getbufsize.__doc__,numpy.geterr.__doc__,numpy.geterrcall.__doc__,numpy.geterrobj.__doc__,numpy.gradient.__doc__,numpy.greater.__doc__,numpy.greater_equal.__doc__,numpy.half.__doc__,numpy.hamming.__doc__,numpy.hanning.__doc__,numpy.heaviside.__doc__,numpy.histogram.__doc__,numpy.histogram2d.__doc__,numpy.histogram_bin_edges.__doc__,numpy.histogramdd.__doc__,numpy.hsplit.__doc__,numpy.hstack.__doc__,numpy.hypot.__doc__,numpy.i0.__doc__,numpy.identity.__doc__,numpy.iinfo.__doc__,numpy.imag.__doc__,numpy.in1d.__doc__,numpy.index_exp.__doc__,numpy.indices.__doc__,numpy.inexact.__doc__,numpy.inf.__doc__,numpy.info.__doc__,numpy.infty.__doc__,numpy.inner.__doc__,numpy.insert.__doc__,numpy.int0.__doc__,numpy.int16.__doc__,numpy.int32.__doc__,numpy.int64.__doc__,numpy.int8.__doc__,numpy.int_.__doc__,numpy.intc.__doc__,numpy.integer.__doc__,numpy.interp.__doc__,numpy.intersect1d.__doc__,numpy.intp.__doc__,numpy.invert.__doc__,numpy.is_busday.__doc__,numpy.isclose.__doc__,numpy.iscomplex.__doc__,numpy.iscomplexobj.__doc__,numpy.isfinite.__doc__,numpy.isfortran.__doc__,numpy.isin.__doc__,numpy.isinf.__doc__,numpy.isnan.__doc__,numpy.isnat.__doc__,numpy.isneginf.__doc__,numpy.isposinf.__doc__,numpy.isreal.__doc__,numpy.isrealobj.__doc__,numpy.isscalar.__doc__,numpy.issctype.__doc__,numpy.issubclass_.__doc__,numpy.issubdtype.__doc__,numpy.issubsctype.__doc__,numpy.iterable.__doc__,numpy.ix_.__doc__,numpy.kaiser.__doc__,numpy.kron.__doc__,numpy.lcm.__doc__,numpy.ldexp.__doc__,numpy.left_shift.__doc__,numpy.less.__doc__,numpy.less_equal.__doc__,numpy.lexsort.__doc__,numpy.lib.__doc__,numpy.linalg.__doc__,numpy.linspace.__doc__,numpy.little_endian.__doc__,numpy.load.__doc__,numpy.loadtxt.__doc__,numpy.log.__doc__,numpy.log10.__doc__,numpy.log1p.__doc__,numpy.log2.__doc__,numpy.logaddexp.__doc__,numpy.logaddexp2.__doc__,numpy.logical_and.__doc__,numpy.logical_not.__doc__,numpy.logical_or.__doc__,numpy.logical_xor.__doc__,numpy.logspace.__doc__,numpy.longcomplex.__doc__,numpy.longdouble.__doc__,numpy.longfloat.__doc__,numpy.longlong.__doc__,numpy.lookfor.__doc__,numpy.ma.__doc__,numpy.mask_indices.__doc__,numpy.mat.__doc__,numpy.math.__doc__,numpy.matmul.__doc__,numpy.matrix.__doc__,numpy.matrixlib.__doc__,numpy.max.__doc__,numpy.maximum.__doc__,numpy.maximum_sctype.__doc__,numpy.may_share_memory.__doc__,numpy.mean.__doc__,numpy.median.__doc__,numpy.memmap.__doc__,numpy.meshgrid.__doc__,numpy.mgrid.__doc__,numpy.min.__doc__,numpy.min_scalar_type.__doc__,numpy.minimum.__doc__,numpy.mintypecode.__doc__,numpy.mod.__doc__,numpy.modf.__doc__,numpy.moveaxis.__doc__,numpy.msort.__doc__,numpy.multiply.__doc__,numpy.nan.__doc__,numpy.nan_to_num.__doc__,numpy.nanargmax.__doc__,numpy.nanargmin.__doc__,numpy.nancumprod.__doc__,numpy.nancumsum.__doc__,numpy.nanmax.__doc__,numpy.nanmean.__doc__,numpy.nanmedian.__doc__,numpy.nanmin.__doc__,numpy.nanpercentile.__doc__,numpy.nanprod.__doc__,numpy.nanquantile.__doc__,numpy.nanstd.__doc__,numpy.nansum.__doc__,numpy.nanvar.__doc__,numpy.nbytes.__doc__,numpy.ndarray.__doc__,numpy.ndenumerate.__doc__,numpy.ndim.__doc__,numpy.ndindex.__doc__,numpy.nditer.__doc__,numpy.negative.__doc__,numpy.nested_iters.__doc__,numpy.newaxis.__doc__,numpy.nextafter.__doc__,numpy.nonzero.__doc__,numpy.not_equal.__doc__,numpy.numarray.__doc__,numpy.number.__doc__,numpy.obj2sctype.__doc__,numpy.object0.__doc__,numpy.object_.__doc__,numpy.ogrid.__doc__,numpy.oldnumeric.__doc__,numpy.ones.__doc__,numpy.ones_like.__doc__,numpy.os.__doc__,numpy.outer.__doc__,numpy.packbits.__doc__,numpy.pad.__doc__,numpy.partition.__doc__,numpy.percentile.__doc__,numpy.pi.__doc__,numpy.piecewise.__doc__,numpy.place.__doc__,numpy.poly.__doc__,numpy.poly1d.__doc__,numpy.polyadd.__doc__,numpy.polyder.__doc__,numpy.polydiv.__doc__,numpy.polyfit.__doc__,numpy.polyint.__doc__,numpy.polymul.__doc__,numpy.polynomial.__doc__,numpy.polysub.__doc__,numpy.polyval.__doc__,numpy.positive.__doc__,numpy.power.__doc__,numpy.printoptions.__doc__,numpy.prod.__doc__,numpy.product.__doc__,numpy.promote_types.__doc__,numpy.ptp.__doc__,numpy.put.__doc__,numpy.put_along_axis.__doc__,numpy.putmask.__doc__,numpy.quantile.__doc__,numpy.r_.__doc__,numpy.rad2deg.__doc__,numpy.radians.__doc__,numpy.random.__doc__,numpy.ravel.__doc__,numpy.ravel_multi_index.__doc__,numpy.real.__doc__,numpy.real_if_close.__doc__,numpy.rec.__doc__,numpy.recarray.__doc__,numpy.recfromcsv.__doc__,numpy.recfromtxt.__doc__,numpy.reciprocal.__doc__,numpy.record.__doc__,numpy.remainder.__doc__,numpy.repeat.__doc__,numpy.require.__doc__,numpy.reshape.__doc__,numpy.resize.__doc__,numpy.result_type.__doc__,numpy.right_shift.__doc__,numpy.rint.__doc__,numpy.roll.__doc__,numpy.rollaxis.__doc__,numpy.roots.__doc__,numpy.rot90.__doc__,numpy.round.__doc__,numpy.round_.__doc__,numpy.row_stack.__doc__,numpy.s_.__doc__,numpy.safe_eval.__doc__,numpy.save.__doc__,numpy.savetxt.__doc__,numpy.savez.__doc__,numpy.savez_compressed.__doc__,numpy.sctype2char.__doc__,numpy.sctypeDict.__doc__,numpy.sctypes.__doc__,numpy.searchsorted.__doc__,numpy.select.__doc__,numpy.set_numeric_ops.__doc__,numpy.set_printoptions.__doc__,numpy.set_string_function.__doc__,numpy.setbufsize.__doc__,numpy.setdiff1d.__doc__,numpy.seterr.__doc__,numpy.seterrcall.__doc__,numpy.seterrobj.__doc__,numpy.setxor1d.__doc__,numpy.shape.__doc__,numpy.shares_memory.__doc__,numpy.short.__doc__,numpy.show_config.__doc__,numpy.sign.__doc__,numpy.signbit.__doc__,numpy.signedinteger.__doc__,numpy.sin.__doc__,numpy.sinc.__doc__,numpy.single.__doc__,numpy.singlecomplex.__doc__,numpy.sinh.__doc__,numpy.size.__doc__,numpy.sometrue.__doc__,numpy.sort.__doc__,numpy.sort_complex.__doc__,numpy.source.__doc__,numpy.spacing.__doc__,numpy.split.__doc__,numpy.sqrt.__doc__,numpy.square.__doc__,numpy.squeeze.__doc__,numpy.stack.__doc__,numpy.std.__doc__,numpy.str0.__doc__,numpy.str_.__doc__,numpy.string_.__doc__,numpy.subtract.__doc__,numpy.sum.__doc__,numpy.swapaxes.__doc__,numpy.sys.__doc__,numpy.take.__doc__,numpy.take_along_axis.__doc__,numpy.tan.__doc__,numpy.tanh.__doc__,numpy.tensordot.__doc__,numpy.test.__doc__,numpy.testing.__doc__,numpy.tile.__doc__,numpy.timedelta64.__doc__,numpy.trace.__doc__,numpy.tracemalloc_domain.__doc__,numpy.transpose.__doc__,numpy.trapz.__doc__,numpy.tri.__doc__,numpy.tril.__doc__,numpy.tril_indices.__doc__,numpy.tril_indices_from.__doc__,numpy.trim_zeros.__doc__,numpy.triu.__doc__,numpy.triu_indices.__doc__,numpy.triu_indices_from.__doc__,numpy.true_divide.__doc__,numpy.trunc.__doc__,numpy.typecodes.__doc__,numpy.typename.__doc__,numpy.ubyte.__doc__,numpy.ufunc.__doc__,numpy.uint.__doc__,numpy.uint0.__doc__,numpy.uint16.__doc__,numpy.uint32.__doc__,numpy.uint64.__doc__,numpy.uint8.__doc__,numpy.uintc.__doc__,numpy.uintp.__doc__,numpy.ulonglong.__doc__,numpy.unicode_.__doc__,numpy.union1d.__doc__,numpy.unique.__doc__,numpy.unpackbits.__doc__,numpy.unravel_index.__doc__,numpy.unsignedinteger.__doc__,numpy.unwrap.__doc__,numpy.use_hugepage.__doc__,numpy.ushort.__doc__,numpy.vander.__doc__,numpy.var.__doc__,numpy.vdot.__doc__,numpy.vectorize.__doc__,numpy.version.__doc__,numpy.void.__doc__,numpy.void0.__doc__,numpy.vsplit.__doc__,numpy.vstack.__doc__,numpy.warnings.__doc__,numpy.where.__doc__,numpy.who.__doc__,numpy.zeros.__doc__,numpy.zeros_like.__doc__)

a = zip(numpy_methods , numpy_methods_info)
numpy_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR PANDAS MODULE :
import pandas
pandas_methods = tuple(dir(pandas))

from pandas import Flags,Float32Dtype,Float64Dtype,__deprecated_num_index_names,__dir__,__docformat__,__getattr__,__git_version__,_is_numpy_dev,_libs,_testing,_typing,__all__,_config
from pandas import read_xml,errors,_version,plotting,api,util
from pandas import *
pandas_methods_info = (BooleanDtype.__doc__,Categorical.__doc__,CategoricalDtype.__doc__,CategoricalIndex.__doc__,DataFrame.__doc__,DateOffset.__doc__,DatetimeIndex.__doc__,DatetimeTZDtype.__doc__,ExcelFile.__doc__,ExcelWriter.__doc__,Flags.__doc__,Float32Dtype.__doc__,Float64Dtype.__doc__,pandas.Index.__doc__,Grouper.__doc__,HDFStore.__doc__,Index.__doc__,IndexSlice.__doc__,Int16Dtype.__doc__,Int32Dtype.__doc__,Int64Dtype.__doc__,pandas.Index.__doc__,Int8Dtype.__doc__,Interval.__doc__,IntervalDtype.__doc__,IntervalIndex.__doc__,MultiIndex.__doc__,NA.__doc__,NaT.__doc__,NamedAgg.__doc__,Period.__doc__,PeriodDtype.__doc__,PeriodIndex.__doc__,RangeIndex.__doc__,Series.__doc__,SparseDtype.__doc__,StringDtype.__doc__,Timedelta.__doc__,TimedeltaIndex.__doc__,Timestamp.__doc__,UInt16Dtype.__doc__,UInt32Dtype.__doc__,UInt64Dtype.__doc__,pandas.Index.__doc__,UInt8Dtype.__doc__,__all__.__doc__,__builtins__.__doc__,__cached__.__doc__,__deprecated_num_index_names.__doc__,__dir__.__doc__,__doc__.__doc__,__docformat__.__doc__,__file__.__doc__,__getattr__.__doc__,__git_version__.__doc__,__loader__.__doc__,__name__.__doc__,__package__.__doc__,pandas.__path__.__doc__,__spec__.__doc__,pandas.__version__.__doc__,_config.__doc__,_is_numpy_dev.__doc__,_libs.__doc__,_testing.__doc__,_typing.__doc__,_version.__doc__,api.__doc__,array.__doc__,pandas.arrays.__doc__,bdate_range.__doc__,pandas.compat.__doc__,concat.__doc__,pandas.core.__doc__,crosstab.__doc__,cut.__doc__,date_range.__doc__,describe_option.__doc__,errors.__doc__,eval.__doc__,factorize.__doc__,get_dummies.__doc__,get_option.__doc__,infer_freq.__doc__,interval_range.__doc__,pandas.io.__doc__,isna.__doc__,isnull.__doc__,json_normalize.__doc__,lreshape.__doc__,melt.__doc__,merge.__doc__,merge_asof.__doc__,merge_ordered.__doc__,notna.__doc__,notnull.__doc__,offsets.__doc__,option_context.__doc__,options.__doc__,pandas.__doc__,period_range.__doc__,pivot.__doc__,pivot_table.__doc__,plotting.__doc__,qcut.__doc__,read_clipboard.__doc__,read_csv.__doc__,read_excel.__doc__,read_feather.__doc__,read_fwf.__doc__,read_gbq.__doc__,read_hdf.__doc__,read_html.__doc__,read_json.__doc__,read_orc.__doc__,read_parquet.__doc__,read_pickle.__doc__,read_sas.__doc__,read_spss.__doc__,read_sql.__doc__,read_sql_query.__doc__,read_sql_table.__doc__,read_stata.__doc__,read_table.__doc__,read_xml.__doc__,reset_option.__doc__,set_eng_float_format.__doc__,set_option.__doc__,show_versions.__doc__,test.__doc__,pandas.testing.__doc__,timedelta_range.__doc__,to_datetime.__doc__,to_numeric.__doc__,to_pickle.__doc__,to_timedelta.__doc__,tseries.__doc__,unique.__doc__,util.__doc__,value_counts.__doc__,wide_to_long.__doc__)

a = zip(pandas_methods , pandas_methods_info)
pandas_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR OS MODULE :
import os
os_methods = tuple(dir(os))

from os import *
os_methods_info = (DirEntry.__doc__,F_OK.__doc__,os.GenericAlias.__doc__,os.Mapping.__doc__,os.MutableMapping.__doc__,O_APPEND.__doc__,O_BINARY.__doc__,O_CREAT.__doc__,O_EXCL.__doc__,O_NOINHERIT.__doc__,O_RANDOM.__doc__,O_RDONLY.__doc__,O_RDWR.__doc__,O_SEQUENTIAL.__doc__,O_SHORT_LIVED.__doc__,O_TEMPORARY.__doc__,O_TEXT.__doc__,O_TRUNC.__doc__,O_WRONLY.__doc__,P_DETACH.__doc__,P_NOWAIT.__doc__,P_NOWAITO.__doc__,P_OVERLAY.__doc__,P_WAIT.__doc__,os.PathLike.__doc__,R_OK.__doc__,SEEK_CUR.__doc__,SEEK_END.__doc__,SEEK_SET.__doc__,TMP_MAX.__doc__,W_OK.__doc__,X_OK.__doc__,os._AddedDllDirectory.__doc__,os._Environ.__doc__,os.__all__.__doc__,__builtins__.__doc__,__cached__.__doc__,__doc__.__doc__,__file__.__doc__,__loader__.__doc__,__name__.__doc__,__package__.__doc__,__spec__.__doc__,os._check_methods.__doc__,os._execvpe.__doc__,os._exists.__doc__,os._exit.__doc__,os._fspath.__doc__,os._get_exports_list.__doc__,os._walk.__doc__,os._wrap_close.__doc__,os.abc.__doc__,abort.__doc__,access.__doc__,os.add_dll_directory.__doc__,altsep.__doc__,chdir.__doc__,chmod.__doc__,close.__doc__,closerange.__doc__,cpu_count.__doc__,curdir.__doc__,defpath.__doc__,device_encoding.__doc__,devnull.__doc__,dup.__doc__,dup2.__doc__,environ.__doc__,error.__doc__,execl.__doc__,execle.__doc__,execlp.__doc__,execlpe.__doc__,execv.__doc__,execve.__doc__,execvp.__doc__,execvpe.__doc__,extsep.__doc__,fdopen.__doc__,fsdecode.__doc__,fsencode.__doc__,fspath.__doc__,fstat.__doc__,fsync.__doc__,ftruncate.__doc__,get_exec_path.__doc__,os.get_handle_inheritable.__doc__,get_inheritable.__doc__,get_terminal_size.__doc__,getcwd.__doc__,getcwdb.__doc__,getenv.__doc__,getlogin.__doc__,getpid.__doc__,getppid.__doc__,isatty.__doc__,kill.__doc__,linesep.__doc__,link.__doc__,listdir.__doc__,lseek.__doc__,lstat.__doc__,makedirs.__doc__,mkdir.__doc__,name.__doc__,open.__doc__,pardir.__doc__,path.__doc__,pathsep.__doc__,pipe.__doc__,popen.__doc__,putenv.__doc__,read.__doc__,readlink.__doc__,remove.__doc__,removedirs.__doc__,rename.__doc__,renames.__doc__,replace.__doc__,rmdir.__doc__,scandir.__doc__,sep.__doc__,os.set_handle_inheritable.__doc__,set_inheritable.__doc__,spawnl.__doc__,spawnle.__doc__,spawnv.__doc__,spawnve.__doc__,os.st.__doc__,startfile.__doc__,stat.__doc__,stat_result.__doc__,statvfs_result.__doc__,strerror.__doc__,supports_bytes_environ.__doc__,os.supports_dir_fd.__doc__,os.supports_effective_ids.__doc__,os.supports_fd.__doc__,os.supports_follow_symlinks.__doc__,symlink.__doc__,os.sys.__doc__,system.__doc__,terminal_size.__doc__,times.__doc__,times_result.__doc__,truncate.__doc__,umask.__doc__,uname_result.__doc__,unlink.__doc__,unsetenv.__doc__,urandom.__doc__,utime.__doc__,waitpid.__doc__,waitstatus_to_exitcode.__doc__,walk.__doc__,write.__doc__)

a = zip(os_methods , os_methods_info)
os_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR SCHEDULE MODULE :
import schedule
schedule_methods_ = tuple(dir(schedule))
from schedule import *
schedule_methods_info = (Callable.__doc__,CancelJob.__doc__,Hashable.__doc__,IntervalError.__doc__,Job.__doc__,List.__doc__,Optional.__doc__,ScheduleError.__doc__,ScheduleValueError.__doc__,Scheduler.__doc__,Set.__doc__,Union.__doc__,__builtins__.__doc__,__cached__.__doc__,__doc__.__doc__,__file__.__doc__,__loader__.__doc__,__name__.__doc__,__package__.__doc__,schedule.__path__.__doc__,__spec__.__doc__,cancel_job.__doc__,clear.__doc__,datetime.__doc__,default_scheduler.__doc__,every.__doc__,functools.__doc__,get_jobs.__doc__,idle_seconds.__doc__,jobs.__doc__,logger.__doc__,logging.__doc__,next_run.__doc__,random.__doc__,re.__doc__,repeat.__doc__,run_all.__doc__,run_pending.__doc__,time.__doc__)

a = zip(schedule_methods_ , schedule_methods_info)
schedule_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR COPY MODULE :
import copy
copy_methods_info = (copy.Error.__doc__,copy.copy.__doc__,copy.deepcopy.__doc__)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR RANDOM MODULE : 
import random
random_methods_ = tuple(random.__all__)

from random import * 
random_methods_info = (Random.__doc__,SystemRandom.__doc__,betavariate.__doc__,choice.__doc__,choices.__doc__,expovariate.__doc__,gammavariate.__doc__,gauss.__doc__,getrandbits.__doc__,getstate.__doc__,lognormvariate.__doc__,normalvariate.__doc__,paretovariate.__doc__,randbytes.__doc__,randint.__doc__,random.__doc__,randrange.__doc__,sample.__doc__,seed.__doc__,setstate.__doc__,shuffle.__doc__,triangular.__doc__,uniform.__doc__,vonmisesvariate.__doc__,weibullvariate.__doc__)

a = zip(random_methods_ , random_methods_info)
random_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
#? FOR COLLECTIONS MODULE :

chainmap_methods_ = ('clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'new_child', 'parents', 'pop', 'popitem', 'setdefault', 'update', 'values')
counter_methods_ = ('clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'total', 'update', 'values')
orderdict_methods_ = ('clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'move_to_end', 'pop', 'popitem', 'setdefault', 'update', 'values')
userdict_methods_ = ('clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values')
userlist_methods_ = ('append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort')
userstring_methods_ = ('capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill')
defaultdict_methods_ = ('clear', 'copy', 'default_factory', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values')
deque_methods_ = ('append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate')

from collections import *
chainmap_methods_info = (ChainMap.clear.__doc__,ChainMap.copy.__doc__,ChainMap.fromkeys.__doc__,ChainMap.get.__doc__,ChainMap.items.__doc__,ChainMap.keys.__doc__,ChainMap.new_child.__doc__,ChainMap.parents.__doc__,ChainMap.pop.__doc__,ChainMap.popitem.__doc__,ChainMap.setdefault.__doc__,ChainMap.update.__doc__,ChainMap.values.__doc__) 
counter_methods_info = (Counter.clear.__doc__,Counter.copy.__doc__,Counter.elements.__doc__,Counter.fromkeys.__doc__,Counter.get.__doc__,Counter.items.__doc__,Counter.keys.__doc__,Counter.most_common.__doc__,Counter.pop.__doc__,Counter.popitem.__doc__,Counter.setdefault.__doc__,Counter.subtract.__doc__,Counter.total.__doc__,Counter.update.__doc__,Counter.values.__doc__) 
orderdict_methods_info = (OrderedDict.clear.__doc__,OrderedDict.copy.__doc__,OrderedDict.fromkeys.__doc__,OrderedDict.get.__doc__,OrderedDict.items.__doc__,OrderedDict.keys.__doc__,OrderedDict.move_to_end.__doc__,OrderedDict.pop.__doc__,OrderedDict.popitem.__doc__,OrderedDict.setdefault.__doc__,OrderedDict.update.__doc__,OrderedDict.values.__doc__) 
userdict_methods_info = (UserDict.clear.__doc__,dict.copy.__doc__,dict.fromkeys.__doc__,UserDict.get.__doc__,UserDict.items.__doc__,UserDict.keys.__doc__,UserDict.pop.__doc__,UserDict.popitem.__doc__,UserDict.setdefault.__doc__,UserDict.update.__doc__,UserDict.values.__doc__) 
userlist_methods_info = (list.append.__doc__,list.clear.__doc__,list.copy.__doc__,list.count.__doc__,list.extend.__doc__,list.index.__doc__,list.insert.__doc__,list.pop.__doc__,list.remove.__doc__,list.reverse.__doc__,list.sort.__doc__) 
userstring_methods_info = (str.capitalize.__doc__,str.casefold.__doc__,str.center.__doc__,str.count.__doc__,str.encode.__doc__,str.endswith.__doc__,str.expandtabs.__doc__,str.find.__doc__,str.format.__doc__,str.format_map.__doc__,str.index.__doc__,str.isalnum.__doc__,str.isalpha.__doc__,str.isascii.__doc__,str.isdecimal.__doc__,str.isdigit.__doc__,str.isidentifier.__doc__,str.islower.__doc__,str.isnumeric.__doc__,str.isprintable.__doc__,str.isspace.__doc__,str.istitle.__doc__,str.isupper.__doc__,str.join.__doc__,str.ljust.__doc__,str.lower.__doc__,str.lstrip.__doc__,UserString.maketrans.__doc__,str.partition.__doc__,str.removeprefix.__doc__,str.removesuffix.__doc__,str.replace.__doc__,str.rfind.__doc__,str.rindex.__doc__,str.rjust.__doc__,str.rpartition.__doc__,str.rsplit.__doc__,str.rstrip.__doc__,str.split.__doc__,str.splitlines.__doc__,str.startswith.__doc__,str.strip.__doc__,str.swapcase.__doc__,str.title.__doc__,str.translate.__doc__,str.upper.__doc__,str.zfill.__doc__) 
defaultdict_methods_info = (defaultdict.clear.__doc__,defaultdict.copy.__doc__,defaultdict.default_factory.__doc__,defaultdict.fromkeys.__doc__,defaultdict.get.__doc__,defaultdict.items.__doc__,defaultdict.keys.__doc__,defaultdict.pop.__doc__,defaultdict.popitem.__doc__,defaultdict.setdefault.__doc__,defaultdict.update.__doc__,defaultdict.values.__doc__) 
deque_methods_info = (deque.append.__doc__,deque.appendleft.__doc__,deque.clear.__doc__,deque.copy.__doc__,deque.count.__doc__,deque.extend.__doc__,deque.extendleft.__doc__,deque.index.__doc__,deque.insert.__doc__,deque.maxlen.__doc__,deque.pop.__doc__,deque.popleft.__doc__,deque.remove.__doc__,deque.reverse.__doc__,deque.rotate.__doc__) 

import collections
collections_all_classes_list = tuple(collections.__all__)

from collections import *
collections_all_classes_info = (ChainMap.__doc__,Counter.__doc__,OrderedDict.__doc__,UserDict.__doc__,UserList.__doc__,UserString.__doc__,defaultdict.__doc__,deque.__doc__,collections.namedtuple.__doc__)

collections_all_classes_methods_list = [chainmap_methods_ ,counter_methods_,orderdict_methods_,userdict_methods_,userlist_methods_,userstring_methods_,defaultdict_methods_,deque_methods_ ,[]]

collections_all_classes_methods_info = [chainmap_methods_info ,counter_methods_info,orderdict_methods_info,userdict_methods_info,userlist_methods_info,userstring_methods_info,defaultdict_methods_info,deque_methods_info ,[]]

a = zip(collections_all_classes_list , collections_all_classes_info , collections_all_classes_methods_list , collections_all_classes_methods_info)
collections_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 

#? FOR DATETIME MODULE :

class date_:
    """Concrete date type.

    Constructors:

    __new__()
    fromtimestamp()
    today()
    fromordinal()

    Operators:

    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__
    __add__, __radd__, __sub__ (add/radd only with timedelta arg)

    Methods:

    timetuple()
    toordinal()
    weekday()
    isoweekday(), isocalendar(), isoformat()
    ctime()
    strftime()

    Properties (readonly):
    year, month, day
    """
    def isocalendar(self):
        """Return a named tuple containing ISO year, week number, and weekday.

        The first ISO week of the year is the (Mon-Sun) week
        containing the year's first Thursday; everything else derives
        from that.

        The first week is 1; Monday is 1 ... Sunday is 7.

        """
    pass

class timedelta_:
    """Represent the difference between two datetime objects.

    Supported operators:

    - add, subtract timedelta
    - unary plus, minus, abs
    - compare to timedelta
    - multiply, divide by int

    In addition, datetime supports subtraction of two datetime objects
    returning a timedelta, and addition or subtraction of a datetime
    and a timedelta giving a datetime.

    Representation: (days, seconds, microseconds).  Why?  Because I
    felt like it.
    """
    pass

class tzinfo_:
    """Abstract base class for time zone info classes.

    Subclasses must override the name(), utcoffset() and dst() methods.
    """
    __slots__ = ()

    def tzname(self):
        "datetime -> string name of time zone."
        raise NotImplementedError("tzinfo subclass must override tzname()")

    def utcoffset(self):
        "datetime -> timedelta, positive for east of UTC, negative for west of UTC"
        raise NotImplementedError("tzinfo subclass must override utcoffset()")

    def dst(self):
        """datetime -> DST offset as timedelta, positive for east of UTC.

        Return 0 if DST not in effect.  utcoffset() must include the DST
        offset.
        """
        raise NotImplementedError("tzinfo subclass must override dst()")

    def fromutc(self):
        "datetime in UTC -> datetime in local time."

    pass

class timezone_(tzinfo_) :
    pass

class time_:
    """Time with time zone.

    Constructors:

    __new__()

    Operators:

    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__

    Methods:

    strftime()
    isoformat()
    utcoffset()
    tzname()
    dst()

    Properties (readonly):
    hour, minute, second, microsecond, tzinfo, fold

    """ 

import datetime 

from datetime import date
datetime_date_info = (date.ctime.__doc__,date.day.__doc__,date.fromisocalendar.__doc__,date.fromisoformat.__doc__,date.fromordinal.__doc__,date.fromtimestamp.__doc__,date.isocalendar.__doc__,date.isoformat.__doc__,date.isoweekday.__doc__,date.max.__doc__,date.min.__doc__,date.month.__doc__,date.replace.__doc__,date.resolution.__doc__,date.strftime.__doc__,date.timetuple.__doc__,date.today.__doc__,date.toordinal.__doc__,date.weekday.__doc__,date.year.__doc__) 

from datetime import datetime
datetime_datetime_info = (datetime.astimezone.__doc__,datetime.combine.__doc__,datetime.ctime.__doc__,datetime.date.__doc__,datetime.day.__doc__,datetime.dst.__doc__,datetime.fold.__doc__,datetime.fromisocalendar.__doc__,datetime.fromisoformat.__doc__,datetime.fromordinal.__doc__,datetime.fromtimestamp.__doc__,datetime.hour.__doc__,datetime.isocalendar.__doc__,datetime.isoformat.__doc__,datetime.isoweekday.__doc__,datetime.max.__doc__,datetime.microsecond.__doc__,datetime.min.__doc__,datetime.minute.__doc__,datetime.month.__doc__,datetime.now.__doc__,datetime.replace.__doc__,datetime.resolution.__doc__,datetime.second.__doc__,datetime.strftime.__doc__,datetime.strptime.__doc__,datetime.time.__doc__,datetime.timestamp.__doc__,datetime.timetuple.__doc__,datetime.timetz.__doc__,datetime.today.__doc__,datetime.toordinal.__doc__,datetime.tzinfo.__doc__,datetime.tzname.__doc__,datetime.utcfromtimestamp.__doc__,datetime.utcnow.__doc__,datetime.utcoffset.__doc__,datetime.utctimetuple.__doc__,datetime.weekday.__doc__,datetime.year.__doc__)

from datetime import time
datetime_time_info = (time.dst.__doc__,time.fold.__doc__,time.fromisoformat.__doc__,time.hour.__doc__,time.isoformat.__doc__,time.max.__doc__,time.microsecond.__doc__,time.min.__doc__,time.minute.__doc__,time.replace.__doc__,time.resolution.__doc__,time.second.__doc__,time.strftime.__doc__,time.tzinfo.__doc__,time.tzname.__doc__,time.utcoffset.__doc__)

from datetime import timedelta
datetime_timedelta_info = (timedelta.days.__doc__,timedelta.max.__doc__,timedelta.microseconds.__doc__,timedelta.min.__doc__,timedelta.resolution.__doc__,timedelta.seconds.__doc__,timedelta.total_seconds.__doc__)

datetime_tzinfo_info = (tzinfo_.dst.__doc__,tzinfo_.fromutc.__doc__,tzinfo_.tzname.__doc__,tzinfo_.utcoffset.__doc__)

from datetime import timezone
datetime_timezone_info = (timezone_.dst.__doc__,timezone_.fromutc.__doc__,timezone.max.__doc__,timezone.min.__doc__,timezone_.tzname.__doc__,timezone.utc.__doc__,timezone_.utcoffset.__doc__)

datetime_date_list = ("ctime","day","fromisocalendar","fromisoformat","fromordinal","fromtimestamp","isocalendar","isoformat","isoweekday","max","min","month","replace","resolution","strftime","timetuple","today","toordinal","weekday","year") 

datetime_datetime_list = ("astimezone","combine","ctime","date","day","dst","fold","fromisocalendar","fromisoformat","fromordinal","fromtimestamp","hour","isocalendar","isoformat","isoweekday","max","microsecond","min","minute","month","now","replace","resolution","second","strftime","strptime","time","timestamp","timetuple","timetz","today","toordinal","tzinfo","tzname","utcfromtimestamp","utcnow","utcoffset","utctimetuple","weekday","year")

datetime_time_list = ("dst","fold","fromisoformat","hour","isoformat","max","microsecond","min","minute","replace","resolution","second","strftime","tzinfo","tzname","utcoffset")

datetime_timedelta_list = ("days","max","microseconds","min","resolution","seconds","total_seconds")

datetime_tzinfo_list = ("dst","fromutc","tzname","utcoffset")

datetime_timezone_list = ("dst","fromutc","max","min","tzname","utc","utcoffset")

import datetime
datetime_all_classes_list = tuple(datetime.__all__)

datetime_all_classes_info = (date_.__doc__,datetime.datetime.__doc__,time_.__doc__,timedelta_.__doc__,timezone_.__doc__,tzinfo_.__doc__,datetime.MINYEAR,datetime.MAXYEAR)

datetime_all_classes_methods_list = (datetime_date_list,datetime_datetime_list,datetime_time_list,datetime_timedelta_list,datetime_timezone_list,datetime_tzinfo_list,[],[])

datetime_all_classes_methods_info = (datetime_date_info,datetime_datetime_info,datetime_time_info,datetime_timedelta_info,datetime_timezone_info,datetime_tzinfo_info,[],[])

a = zip(datetime_all_classes_list , datetime_all_classes_info , datetime_all_classes_methods_list , datetime_all_classes_methods_info)
datetime_data = tuple(a)

# ------------------------------------------------------------------------------------------------------------------------------------ 
