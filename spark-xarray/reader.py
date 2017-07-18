from __future__ import print_function
import numpy as np
import pandas as pd 
import xarray as xr
from pyspark.sql import SparkSession


def ncread(sc, file_list, mode='single', partitions=None, partition_on='time'):
    if (mode == 'single') and (partition_on == 'time'):
        return read_nc_single_time(sc, file_list, partitions)

    elif mode == 'multi':
        pass 

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
            .map(lambda x: readonetimestep(dset, x))

    return rdd 

def readonetimestep(dset, timestep):
    chunk = dset.sel(time=timestep)
    return chunk



if __name__ == '__main__':
    spark = SparkSession.builder.appName('hi').getOrCreate()
    sc = spark.sparkContext

    filename = '../sample-data/air.sig995.2012.nc'

    rdd = ncread(sc, filename, mode='single')
    print(rdd.count())
    print(rdd.first())
    print(rdd.getNumPartitions())
  



    

    



