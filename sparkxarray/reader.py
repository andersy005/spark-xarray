
# MIT License
#
# Copyright (c) 2017 Anderson Banihirwe
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function
from __future__ import absolute_import
import os
import numpy as np
import pandas as pd 
import xarray as xr
import itertools
from glob import glob
from pyspark.sql import SparkSession


def ncread(sc, paths, mode='single', **kwargs):
    """Calls sparkxarray netcdf read function based on the mode parameter.

    ============ ==============================
    Mode          Reading Function
    ------------ ------------------------------
    single       : read_nc_single
    multi        : read_nc_multi
    Anything else: Throw an exception
    ============= ==============================

    Parameters
    ----------

    sc       :  sparkContext object

    paths    :  str or sequence
                Either a string glob in the form "path/to/my/files/*.nc" or an explicit
                list of files to open

    mode     : str
               'single' for a single file
               'multi' for multiple files

    **kwargs : dict
               partitioning options to be passed on to the actual read function.
            
    
    """

    if 'partitions' not in kwargs:
        kwargs['partitions'] = None

    if 'partition_on' not in kwargs:
        kwargs['partition_on'] = ['time']

    error_msg = ("You specified a mode that is not implemented.")

    if (mode == 'single'):
        return read_nc_single(sc, paths, **kwargs)

    elif (mode == 'multi'):
        return read_nc_multi(sc, paths, **kwargs)
    else:
        raise NotImplementedError(error_msg)

        
def read_nc_single(sc, paths, **kwargs):
    """ Read a single netCDF file

    Parameters
    -----------
    sc       :  sparkContext object

    paths    :  str
                an explicit filename to open
    

    **kwargs : dict
               Additional arguments for partitioning 

    """
    partition_on = kwargs.get('partition_on')
    partitions = kwargs.get('partitions')

    dset = xr.open_dataset(paths)

    # D = {'dim_1': dim_1_size, 'dim_2': dim_2_size, ...}
    D ={dset[dimension].name:dset[dimension].size for dimension in partition_on}
    
    # dim_sizes = [range(dim_1_size), range(dim_2_size), range(...)]
    dim_ranges = [range(dim_size) for dim_size in D.values()]
    

    dim_cartesian_product_indices = [element for element in itertools.product(*dim_ranges)]

    # create a list of dictionaries for  positional indexing
    positional_indices = [dict(zip(partition_on, ij)) for ij in dim_cartesian_product_indices]

    if not partitions:
        partitions = len(dim_cartesian_product_indices) / 50

    if partitions > len(dim_cartesian_product_indices):
        partitions = len(dim_cartesian_product_indices)

    
    # Create an RDD
    rdd = sc.parallelize(positional_indices, partitions).map(lambda x: readone_slice(dset, x))

    return rdd


def readone_slice(dset, positional_indices):
    """Read a slice from an xarray.Dataset.

    Parameters
    ----------

    dset                : file_object
                         xarray.Dataset object
    positional_indices  : dict
                          dict containing positional indices for each dimension
                          e.g. {'lat': 0, 'lon': 0}

    Returns
    ---------
    chunk               : xarray.Dataset
                         a subset of the Xarray Dataset

    """

    # Change the positional indices into slice objects
    # e.g {'lat': 0, 'lon': 0} ---> {'lat': slice(0, 1, None),  'lon': slice(0, 1, None)}
    positional_slices = {dim: slice(positional_indices[dim], positional_indices[dim]+1) 
                                                         for dim in positional_indices}

    # Read a slice for the given positional_slices
    chunk = dset[positional_slices]
    return chunk


def read_nc_multi(sc, paths, **kwargs):
    """ Read multiple netCDF files

    Parameters
    -----------
    sc       :  sparkContext object

    paths    :  str or sequence
                Either a string glob in the form "path/to/my/files/*.nc" or an explicit
                list of files to open

    **kwargs : dict
               Additional arguments for partitioning 

    """

    partition_on = kwargs.get('partition_on')
    partitions = kwargs.get('partitions')

    dset = xr.open_mfdataset(paths, autoclose=True)

    # D = {'dim_1': dim_1_size, 'dim_2': dim_2_size, ...}
    D ={dset[dimension].name:dset[dimension].size for dimension in partition_on}
    
    # dim_sizes = [range(dim_1_size), range(dim_2_size), range(...)]
    dim_ranges = [range(dim_size) for dim_size in D.values()]
    

    dim_cartesian_product_indices = [element for element in itertools.product(*dim_ranges)]

    # create a list of dictionaries for  positional indexing
    positional_indices = [dict(zip(partition_on, ij)) for ij in dim_cartesian_product_indices]

    if not partitions:
        partitions = len(dim_cartesian_product_indices) / 50

    if partitions > len(dim_cartesian_product_indices):
        partitions = len(dim_cartesian_product_indices)

    
    # Create an RDD
    rdd = sc.parallelize(positional_indices, partitions).map(lambda x: readone_slice(dset, x))

    return rdd

