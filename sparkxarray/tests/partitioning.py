from pyspark.sql import SparkSession 
from sparkxarray.reader import ncread
import os


spark = SparkSession.builder.appName('hi').getOrCreate()
sc = spark.sparkContext
print(os.getcwd())
filename = os.path.abspath('tests/data/air.sig995.2012.nc')
print(filename)

#rdd = ncread(sc, filename, mode='single', partition_on='grid')
#print(rdd.count())
#print(rdd.first())
#print(rdd.getNumPartitions())
#print(('################'))
rdd1 = ncread(sc, filename, mode='single', partition_on='time')
print(rdd1.count())
print(rdd1.first())
print(rdd1.getNumPartitions())
    
"""
filepath = '/Users/abanihi/Documents/netCDF-datasets/NCEP-OI/*.nc'
#rdd = ncread(sc, filepath, mode='multi', partition_on='time')
rdd = nc_multi_read(sc, filepath, data_splitting_mode='slice')
print(rdd.count())
print(type(rdd.first()))
"""





