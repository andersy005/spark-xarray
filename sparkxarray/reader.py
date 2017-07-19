from __future__ import print_function
import numpy as np
import pandas as pd 
import xarray as xr
import itertools
from glob import glob
from pyspark.sql import SparkSession


def ncread(sc, filename, mode='single', partitions=None, partition_on='time'):
    if (mode == 'single') and (partition_on == 'time'):
        return read_nc_single_time(sc, filename, partitions)
    elif (mode == 'single') and (partition_on == 'grid'):
        return read_nc_single_grid(sc, filename, partitions)
    else:
        raise NotImplementedError("You specified a mode that is not implemented.")

def nc_multi_read(sc, file_list, partitions=None, data_splitting_mode='slice'):
    if (data_splitting_mode == 'slice'):
        return read_nc_multi_time_slice(sc, file_list, partitions) 
        
    elif (data_splitting_mode == 'series'):
        return read_nc_multi_series(sc, file_list, partitions) 
    else:
        raise NotImplementedError("You specified a mode that is not implemented.")

def read_nc_single_time(sc, filename, partitions):
    dset = xr.open_dataset(filename)

    # Get all time steps
    timesteps = dset.time

    if not partitions:
        partitions = timesteps.size / 6

    if partitions > timesteps.size:
        partitions = timesteps.size

    rdd = sc.parallelize(timesteps.values, partitions)\
            .map(lambda x: readone_timestep(dset, x))

    return rdd 

def readone_timestep(dset, timestep):
    chunk = dset.sel(time=timestep)
    return chunk


def read_nc_single_grid(sc, filename, partitions):
     
    dset = xr.open_dataset(filename)

    # Get latitude and longitude values
    lats = dset.lat.values
    lons = dset.lon.values
    grid_points = [element for element in itertools.product(lats, lons)]

    if not partitions:
        partitions = len(grid_points) / 20 

    if partitions > len(grid_points):
        partitions = len(grid_points)

    rdd = sc.parallelize(grid_points, partitions)\
            .map(lambda x: readone_gridpoint(dset, x))

    return rdd


def readone_gridpoint(dset, grid_point):
    chunk = dset.sel(lat=grid_point[0], lon=grid_point[1])
    return chunk

def read_nc_multi_time_slice(sc, paths, partitions):
    if isinstance(paths, list):
        file_list = paths
    elif isinstance(paths, str):
        file_list = sorted(glob(paths))
    
    if not partitions:
        partitions = len(file_list) / 20

    if partitions > len(file_list):
        partitions = len(file_list)

    rdd = sc.parallelize(file_list, partitions)\
           .map(lambda filename: readones(filename))

    return rdd
        
def readones(filename):
    dset = xr.open_dataset(filename)
    return dset

def read_nc_multi_series(sc, file_list, partitions):
    pass


if __name__ == '__main__':
    spark = SparkSession.builder.appName('hi').getOrCreate()
    sc = spark.sparkContext
    """
    filename = '../sample-data/air.sig995.2012.nc'

    rdd = ncread(sc, filename, mode='single', partition_on='grid')
    print(rdd.count())
    print(rdd.first())
    print(rdd.getNumPartitions())
    """

    filepath = '/Users/abanihi/Documents/netCDF-datasets/NCEP-OI/*.nc'
    #rdd = ncread(sc, filepath, mode='multi', partition_on='time')
    rdd = nc_multi_read(sc, filepath, data_splitting_mode='slice')
    print(rdd.count())
    print(type(rdd.first()))






