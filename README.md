[![Build Status](https://travis-ci.org/andersy005/spark-xarray.svg?branch=master)](https://travis-ci.org/andersy005/spark-xarray)
[![codecov](https://codecov.io/gh/andersy005/spark-xarray/branch/master/graph/badge.svg)](https://codecov.io/gh/andersy005/spark-xarray)

# spark-xarray
This is an experimental project that seeks to integrate PySpark and xarray for Climate Data Analysis.


## Overview
Spark-xarray is a high level, Apache Spark, xarray-based Python library for working with netCDF climate model data with Apache Spark. It is designed to work mainly with big climate datasets, such as global weather data over several years at spatial resolutions down to e.g. 0.1 x 0.1 degree resolution.

Spark-xarray was originally conceived during the Summer of 2017 as part of [PySpark for "Big" Atmospheric & Oceanic Data Analysis](https://ncar.github.io/PySpark4Climate/) - [A CISL/SIParCS Research Project](https://www2.cisl.ucar.edu/siparcs).

## Installation

We will guide you how to install spark-xarray. However, we will assume that an Apache Spark installation is available.


### git & pip
Clone the repository directly from GitHub and install it aftwards using ```pip```. This will also resolve possible missing dependencies.

```
git clone https://github.com/andersy005/spark-xarray.git
cd spark-xarray
pip install -e .
```


## General notes

### .bashrc on Linux or .bash_profile on MAC

Make sure the following variables are set in your `.bashrc` or ```.bash_profile```. It is possible, depending on your system configuration, that the following configuration **doesn't have to be applied**.

```bash
# Example of a .bashrc configuration.
export SPARK_HOME=/usr/lib/spark
export PYTHONPATH="$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10-src.zip:$PYTHONPATH"
```

## Getting Started