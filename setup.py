#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages
import os
from ast import parse

LONG_DESCRIPTION = """
**spark-xarray**: 
      
Spark-xarray is a high level, Apache Spark and xarray-based Python library for working 
with netCDF climate model data with Apache Spark.

 Important links
------------------

- Official source code repo: https://github.com/andersy005/spark-xarray
- Issue tracker: https://github.com/andersy005/spark-xarray/issues

"""

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

INSTALL_REQUIRES = (['numpy >= 1.7',
                      'scipy >= 0.16',
                      'pandas >= 0.15.0',
                      'netCDF4 >= 1.2',
                      'xarray>=0.9.5', 
                      'dask >= 0.14',
                      'distributed >= 1.16.1',
                      'geopandas >= 0.3.0', 
                      'toolz>=0.8.2',
                      'cloudpickle >= 0.2.1'])

packages = ['sparkxarray', 'sparkxarray.tests']

package_data = {'sparkxarray': ['data/*.nc']}

setup(name=NAME,
      version=version(),
      author='Anderson Banihirwe, Kevin Paul',
      author_email='axbanihirwe@gmail.com',
      description='Big Atmospheric & Oceanic Data Analysis with Apache Spark + xarray',
      url='https://github.com/andersy005/spark-xarray',
      long_description=LONG_DESCRIPTION,
      install_requires=INSTALL_REQUIRES,
      packages=packages,
      package_data=package_data,
      keywords=[' Climate Science', 'xarray', 'Apache Spark', 'Distributed', 'netCDF', 'Parallel'],
      classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Atmospheric Science'
       ],
      zip_safe=False,
      
)
