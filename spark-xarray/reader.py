from __future__ import print_function
import numpy as np
import pandas as pd 
import xarray as xr
from pyspark.sql import SparkSession

a = xr.open_dataset('../sample-data/air.sig995.2012.nc')
print(a)




