|Build Status| |codecov| |Build status| |License: MIT| |PyPI|

spark-xarray
============

spark-xarray is an open source project and Python package that seeks to
integrate PySpark and xarray for Climate Data Analysis. It is built on
top of `PySpark - Spark Python API`_ and `xarray`_.

spark-xarray was originally conceived during the Summer of 2017 as part
of `PySpark for “Big” Atmospheric & Oceanic Data Analysis`_ - `A
CISL/SIParCS Research Project`_.

It is currently maintained by `Anderson Banihirwe`_.

Documentation is available at
https://andersy005.github.io/spark-xarray/. ## Installation

We will guide you how to install spark-xarray. However, we will assume
that an Apache Spark installation is available.

Install
~~~~~~~

Requirements
^^^^^^^^^^^^

For the installation of ``spark-xarray``, the following packages are
required:

-  `Spark 2.0+`_
-  `netcdf4-python (>=1.2.8)`_
-  ``xarray (>=0.9.5)``
-  ``dask (>=0.15.1)``
-  ``toolz (>=0.8.2)``

Install
^^^^^^^

Clone the repository directly from GitHub and install it aftwards using
``$ python setup.py``. This will also resolve possible missing
dependencies.

.. code:: sh

    $ git clone https://github.com/andersy005/spark-xarray.git
    $ cd spark-xarray
    $ python setup.py install

Development
-----------

We welcome new contributors of all experience levels.

Important links
~~~~~~~~~~~~~~~

-  Official source code repo: https://github.com/andersy005/spark-xarray
-  Issue tracker: https://github.com/andersy005/spark-xarray/issues

Examples
--------

Single file
~~~~~~~~~~~

\`\`\`python >>> from sparkxarray.reader import ncread >>> from
pyspark.sql import SparkSession >>> spark =
SparkSession.builder.appName(‘spark-rdd’).getOrCreate() >>> sc =
spark.SparkContext >>>
filepath=‘spark-xarray/sparkxarray/tests/data/air.sig995.2012.nc’ >>> #
Create an RDD >>> rdd = ncread(sc, filepath, mode=‘single’,
partition\_on=[‘time’], partitions=100) >>> rdd.first() # Get the first
element <xarray.Dataset> Dimensions: (lat: 73, lon: 144, time: 1)
Coordinates: \* lat (lat) float32 90.0 87.5 85.0 82.5 80.0 77.5 75.0
72.5 70.0 67.5 … \* lon (lon) float32 0.0 2.5 5.0 7.5 10.0 12.5 15.0
17.5 20.0 22.5 … \* time (time) datetime64[ns] 2012-01-01 Data variables

.. _PySpark - Spark Python API: https://spark.apache.org/docs/latest/api/python/index.html
.. _xarray: http://xarray.pydata.org/en/stable/
.. _PySpark for “Big” Atmospheric & Oceanic Data Analysis: https://ncar.github.io/PySpark4Climate/
.. _A CISL/SIParCS Research Project: https://www2.cisl.ucar.edu/siparcs
.. _Anderson Banihirwe: https://github.com/andersy005
.. _Spark 2.0+: https://spark.apache.org/
.. _netcdf4-python (>=1.2.8): https://unidata.github.io/netcdf4-python/

.. |Build Status| image:: https://travis-ci.org/andersy005/spark-xarray.svg?branch=master
   :target: https://travis-ci.org/andersy005/spark-xarray
.. |codecov| image:: https://codecov.io/gh/andersy005/spark-xarray/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/andersy005/spark-xarray
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/93dmqmctpjcgnbcs/branch/master?svg=true
   :target: https://ci.appveyor.com/project/andersy005/spark-xarray/branch/master
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-red.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/Django.svg
   :target: .
