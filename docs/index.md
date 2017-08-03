
[![Build Status](https://travis-ci.org/andersy005/spark-xarray.svg?branch=master)](https://travis-ci.org/andersy005/spark-xarray)
[![codecov](https://codecov.io/gh/andersy005/spark-xarray/branch/master/graph/badge.svg)](https://codecov.io/gh/andersy005/spark-xarray)

# spark-xarray

spark-xarray is an open source project and Python package that seeks to integrate PySpark and xarray for Climate Data Analysis. It is built on top of [PySpark - Spark Python API](https://spark.apache.org/docs/latest/api/python/index.html) and [xarray](http://xarray.pydata.org/en/stable/).

spark-xarray was originally conceived during the Summer of 2017 as part of [PySpark for "Big" Atmospheric & Oceanic Data Analysis](https://ncar.github.io/PySpark4Climate/) - [A CISL/SIParCS Research Project](https://www2.cisl.ucar.edu/siparcs).

It is currently maintained by [Anderson Banihirwe](https://github.com/andersy005).

Documentation is available at https://andersy005.github.io/spark-xarray/.
## Installation

We will guide you how to install spark-xarray. However, we will assume that an Apache Spark installation is available.


### Install

#### Requirements

For the installation of ```spark-xarray```, the following packages are required:


- [Spark 2.0+](https://spark.apache.org/)
- [netcdf4-python (>=1.2.8)](https://unidata.github.io/netcdf4-python/)
- ```xarray (>=0.9.5)```
- ```dask (>=0.15.1)```
- ```toolz (>=0.8.2)```

#### Install

Clone the repository directly from GitHub and install it aftwards using ```$ python setup.py```. This will also resolve possible missing dependencies.

```sh
$ git clone https://github.com/andersy005/spark-xarray.git
$ cd spark-xarray
$ python setup.py install
```

## Development

We welcome new contributors of all experience levels.

### Important links

- Official source code repo: https://github.com/andersy005/spark-xarray
- Issue tracker: https://github.com/andersy005/spark-xarray/issues

## Examples

### Single file

```python
>>> from sparkxarray.reader import ncread
>>> from pyspark.sql import SparkSession
>>> spark = SparkSession.builder.appName('spark-rdd').getOrCreate()
>>> sc = spark.SparkContext
>>> filepath='spark-xarray/sparkxarray/tests/data/air.sig995.2012.nc'
>>> # Create an RDD
>>> rdd = ncread(sc, filepath, mode='single', partition_on=['time'], partitions=100)
>>> rdd.first()  # Get the first element
<xarray.Dataset>
Dimensions:  (lat: 73, lon: 144, time: 1)
Coordinates:
  * lat      (lat) float32 90.0 87.5 85.0 82.5 80.0 77.5 75.0 72.5 70.0 67.5 ...
  * lon      (lon) float32 0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5 ...
  * time     (time) datetime64[ns] 2012-01-01
Data variables:
    air      (time, lat, lon) float64 234.5 234.5 234.5 234.5 234.5 234.5 ...
Attributes:
    Conventions:  COARDS
    title:        mean daily NMC reanalysis (2012)
    history:      created 2011/12 by Hoop (netCDF2.3)
    description:  Data is from NMC initialized reanalysis\n(4x/day).  These a...
    platform:     Model
    references:   http://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanaly...
>>> rdd.count()   # Get a count of elements in the rdd
366
>>> # The count above corresponds to number of timesteps in the netCDF file 
>>> rdd.getNumPartitions()  # Get the number of partitions
100
>>> # Compute the daily average for each day (element) in RDD
>>> daily_average = rdd.map(lambda x: x.mean(dim=['lat', 'lon']))
>>> daily_average.take(3)
[<xarray.Dataset>
Dimensions:  (time: 1)
Coordinates:
  * time     (time) datetime64[ns] 2012-01-01
Data variables:
    air      (time) float64 277.0, <xarray.Dataset>
Dimensions:  (time: 1)
Coordinates:
  * time     (time) datetime64[ns] 2012-01-02
Data variables:
    air      (time) float64 276.8, <xarray.Dataset>
Dimensions:  (time: 1)
Coordinates:
  * time     (time) datetime64[ns] 2012-01-03
Data variables:
    air     
```

### Multiple files

```python
>>> from sparkxarray.reader import ncread
>>> from pyspark.sql import SparkSession
>>> spark = SparkSession.builder.appName('spark-rdd').getOrCreate()
>>> sc = spark.SparkContext
>>> paths='spark-xarray/sparkxarray/tests/data/NCEP/*.nc'
>>> multi_rdd = ncread(sc, paths, mode='multi', partition_on=['lat', 'lon'], partitions=300)
>>> multi_rdd.count()
16020
>>> multi_rdd.first()
<xarray.Dataset>
Dimensions:   (lat: 1, lon: 1, nv: 2, time: 4, zlev: 1)
Coordinates:
  * zlev      (zlev) float32 0.0
  * lat       (lat) float32 -88.0
  * lon       (lon) float32 0.0
  * time      (time) datetime64[ns] 1854-01-15 1854-02-15 1854-03-15 1854-04-15
Dimensions without coordinates: nv
Data variables:
    lat_bnds  (time, lat, nv) float32 -89.0 -87.0 -89.0 -87.0 -89.0 -87.0 ...
    lon_bnds  (time, lon, nv) float32 -1.0 1.0 -1.0 1.0 -1.0 1.0 -1.0 1.0
    sst       (time, zlev, lat, lon) float64 nan nan nan nan
    anom      (time, zlev, lat, lon) float64 nan nan nan nan
Attributes:
    Conventions:                CF-1.6
    Metadata_Conventions:       CF-1.6, Unidata Dataset Discovery v1.0
    metadata_link:              C00884
    id:                         ersst.v4.185401
    naming_authority:           gov.noaa.ncdc
    title:                      NOAA Extended Reconstructed Sea Surface Tempe...
    summary:                    ERSST.v4 is developped based on v3b after rev...
    institution:                NOAA/NESDIS/NCDC
    creator_name:               Boyin Huang
    creator_email:              boyin.huang@noaa.gov
    date_created:               2014-10-24
    production_version:         Beta Version 4
    history:                    Version 4 based on Version 3b
    publisher_name:             Boyin Huang
    publisher_email:            boyin.huang@noaa.gov
    publisher_url:              http://www.ncdc.noaa.gov
    creator_url:                http://www.ncdc.noaa.gov
    license:                    No constraints on data access or use
    time_coverage_start:        1854-01-15T000000Z
    time_coverage_end:          1854-01-15T000000Z
    geospatial_lon_min:         -1.0f
    geospatial_lon_max:         359.0f
    geospatial_lat_min:         -89.0f
    geospatial_lat_max:         89.0f
    geospatial_lat_units:       degrees_north
    geospatial_lat_resolution:  2.0
    geospatial_lon_units:       degrees_east
    geospatial_lon_resolution:  2.0
    spatial_resolution:         2.0 degree grid
    cdm_data_type:              Grid
    processing_level:           L4
    standard_name_vocabulary:   CF Standard Name Table v27
    keywords:                   Earth Science &gt; Oceans &gt; Ocean Temperat...
    keywords_vocabulary:        NASA Global Change Master Directory (GCMD) Sc...
    project:                    NOAA Extended Reconstructed Sea Surface Tempe...
    platform:                   Ship and Buoy SSTs from ICOADS R2.5 and NCEP GTS
    instrument:                 Conventional thermometers
    source:                     ICOADS R2.5 SST, NCEP GTS SST, HadISST ice, N...
    comment:                    SSTs were observed by conventional thermomete...
    references:                 Huang et al, 2014: Extended Reconstructed Sea...
    climatology:                Climatology is based on 1971-2000 SST, Xue, Y...
    description:                In situ data: ICOADS2.5 before 2007 and NCEP ...
```
