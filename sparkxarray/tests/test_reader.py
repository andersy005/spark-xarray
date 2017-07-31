from pyspark.sql import SparkSession 
from sparkxarray.reader import ncread
import os


spark = SparkSession.builder.appName('spark-tests').getOrCreate()
sc = spark.sparkContext
print(os.getcwd())
filename = os.path.abspath('sparkxarray/tests/data/air.sig995.2012.nc')
print(filename)
paths = os.path.abspath('sparkxarray/tests/data/NCEP/*.nc')
print(paths)

### Tests for single file
rdd1 = ncread(sc, filename, mode='single', partition_on=['lat', 'lon'], partitions=300)
print(rdd1.count())
print(rdd1.first())
print(rdd1.getNumPartitions())
    

rdd2 = ncread(sc, filename, mode='single', partition_on=['time'], partitions=80)
print(rdd2.count())
print(rdd2.first())


### Tests for Multiple files 
rdd3 = ncread(sc, paths, mode='multi', partition_on=['lat', 'lon'], partitions=300)
print(rdd3.count())
print(rdd3.first())

rdd4 = ncread(sc, paths, mode='multi', partition_on=['lat', 'lon', 'time', 'nv'], partitions=1000)
print(rdd4.count())
print(rdd4.first())








