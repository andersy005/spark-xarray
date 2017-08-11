import xarray as xr 
import dask.array
import numpy as np 
import scipy.stats 


from xarray.core.pycompat import dask_array_type

@xr.register_dataarray_accessor('biascorrect')
class Biascorrect(object):
    def __init__(self, xarray_obj):
        self._obj = xarray_obj


        
