from __future__ import print_function
import numpy as np 
from pyspark.sql import SparkSession



if __name__ == "__main__":
    spark = SparkSession.builder.appName("test").getOrCreate()
    sc = spark.sparkContext
    
    a = np.arange(300).reshape(30, 10)
    rdd = sc.parallelize(a, 10)
    print(rdd.count())
    print(rdd.collect())
    