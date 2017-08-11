import xarray as xr 
import dask.array
import numpy as np 
import scipy.stats 


from xarray.core.pycompat import dask_array_type

@xr.register_dataset_accessor('biascorrect')
class Biascorrect(object):
    def __init__(self, xarray_obj):
        self._obj = xarray_obj
        self._center = None

    @property
    def center(self):
        if self._center is None:
            lon = self._obj.latitude
            lat = self._obj.longitude
            self._center = (float(lon.mean()), float(lat.mean()))

        return self._center

    def plot(self):
        return 'plotting'


        
