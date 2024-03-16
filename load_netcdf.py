# Loading netcdf files and plotting
import numpy as np
import xarray as xr
import dask
import scipy.stats as stats
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import json
import requests
from tqdm import tqdm

# Load netcdf file
def load_netcdf(var, year):
    # Define source filename
    filename = 'DayMet_Gridded_Obs_GTA/' + var + '/' + var + '_' + year + 'subset.nc'
    # Check if file exists
    if os.path.isfile(filename):
        return xr.load_dataset(filename)
    else:
        print('File does not exist')
        exit(0)

ds = load_netcdf('tmax', '2010')
print(ds.keys())