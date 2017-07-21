"""Setup-module for spark-xarray.

This software enables working with netCDF climate model data in Apache Spark.

See: 
https://github.com/andersy005/spark-xarray
"""

import os
import re
import sys
import warnings
from setuptools import setup
from setuptools import find_packages

setup(name='spark-xarray',
      maintainer='Anderson Banihirwe',
      maintainer_email='axbanihirwe@gmail.com',
      version='0.1.dev0',
      description='Big Atmospheric & Oceanic Data Analysis with Apache Spark with xarray',
      url='https://github.com/andersy005/spark-xarray',
      install_requires=['xarray'],
      packages=['sparkxarray'],
      keywords=['xarray', 'Apache Spark', 'Distributed'],
      
)