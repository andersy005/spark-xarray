from pyspark.sql import SparkSession 
from sparkxarray.reader import ncread
import os


spark = SparkSession.builder.appName('hi').getOrCreate()
sc = spark.sparkContext
print(os.getcwd())
filename = os.path.abspath('sparkxarray/tests/data/air.sig995.2012.nc')
print(filename)

rdd1 = ncread(sc, filename, mode='single', partition_on=['lat', 'lon'], partitions=300)
print(rdd1.count())
print(rdd1.first())
print(rdd1.getNumPartitions())
    

rdd2 = ncread(sc, filename, mode='single', partition_on=['time'], partitions=80)
print(rdd2.count())
print(rdd2.first())

rdd3 = ncread(sc, filename, mode='single', partition_on=['time', 'lat', 'lon'], partitions=800)
print(rdd3.count())
print(rdd3.first())





