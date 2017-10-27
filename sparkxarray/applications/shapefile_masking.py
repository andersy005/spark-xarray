# -*- coding: utf-8 -*-
""" Masking an area in a netCDF dataset using a geographical outline.
This module reads a shapefile using geopandas. The user have the option 
of masking the area inside or outside the geographical outline.
"""

import warnings
warnings.filterwarnings('ignore')
import xarray as xr 
import geopandas as gpd 
from geopandas import GeoDataFrame  # Loading boundaries data
from shapely.geometry import Point, Polygon, shape # For creating geospatial data
import time
from functools import partial 


def _shift_lon_values(dset):
    from shapely.geometry import Point 
    lat = dset.lat.values 
    lon = dset.lon.values 

    if lon >= 180:
        lon = lon - 360.

    coordinate = Point(lon, lat)
    return coordinate, dset 
    


def masking(sc, rdd, shapefile_path, mask_area='in'):

    print("Loading and broadcasting the shapefile....\n\n")
    shape = GeoDataFrame.from_file(shapefile_path)

    my_shape = sc.broadcast(shape)
    print("Successfully loaded the shapefile....\n\n")

    print("Masking the data against the shapefile in progress....\n\n")
    start = time.time()
    masked_rdd = rdd.map(_shift_lon_values).filter(partial(_point_look_up, my_shape))\
              .collect()
    masked_data = [item[1] for item in masked_rdd]
    
    dset = xr.auto_combine(masked_data, concat_dim=None)
    
    stop = time.time()
    total_time = stop - start 
    print("Successfully masked the data in {} seconds\n".format(round(total_time, 3)))
    return dset
    


def _point_look_up(my_shape, element):
    grid_point = element[0]
    dset = element[1]

    # Access the broadcasted shape on the workers
    gdf = my_shape.value 

    # See if the grid point i s inside the shape
    check = gdf.contains(grid_point).unique()


    if True in check:
        return True
    else:
        return False
