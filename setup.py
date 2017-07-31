#!/usr/bin/env python

"""Setup-module for spark-xarray.

This software enables working with netCDF climate model data in Apache Spark.

See: 
https://github.com/andersy005/spark-xarray
"""


from setuptools import setup
from setuptools import find_packages
import os
from ast import parse

NAME = 'spark-xarray'

def version():
      """Return version string."""
      with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'sparkxarray', '__init__.py')) as input_file:
            for line in input_file:
                  if line.startswith('__version__'):
                        return parse(line).body[0].value.s


#for line in open('sparkxarray/__init__.py').readlines():
#      if line.startswith('__version__'):
#            exec(line)

INSTALL_REQUIRES = (['xarray>=0.9.5', 'dask'])

packages = ['sparkxarray', 'sparkxarray.examples', 'sparkxarray.tests']

package_data = {'sparkxarray': ['data/*.nc']}

setup(name=NAME,
      version=version(),
      author='Anderson Banihirwe, Kevin Paul',
      maintainer_email='axbanihirwe@gmail.com',
      description='Big Atmospheric & Oceanic Data Analysis with Apache Spark + xarray',
      url='https://github.com/andersy005/spark-xarray',
      long_description="""
      Spark-xarray is a high level, Apache Spark and xarray-based Python library for working 
      with netCDF climate model data with Apache Spark.
      """,
      install_requires=INSTALL_REQUIRES,
      packages=packages,
      package_data=package_data,
      keywords=['xarray', 'Apache Spark', 'Distributed', 'netCDF', 'Parallel'],
      zip_safe=False,
      
)