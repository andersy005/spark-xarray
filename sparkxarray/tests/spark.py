from __future__ import print_function
import numpy as np 
from pyspark.sql import SparkSession
import xarray as xr




if __name__ == "__main__":
    spark = SparkSession.builder.appName("test").getOrCreate()
    sc = spark.sparkContext

    data = xr.DataArray(np.random.randn(2, 200), coords={'x': ['a', 'b']}, dims=('x', 'y'))
    print(type(data))
    rdd = sc.parallelize(data, 10)
    print(rdd.count())
    print(rdd.take(2))
    