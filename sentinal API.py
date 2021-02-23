#######################################################
#Date:      Feb 2 2021#
#Name:      Robert Simon Irving#
#Purpose:   SentinelSat API#
#           COGS Project 2021#
#######################################################
#======================================================#
#1. Import Modules
#======================================================#
import os
import numpy as np
import sentinelsat
import datetime
import shutil
#import folium
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sentinelsat.sentinel import SentinelAPI
from sentinelsat.sentinel import read_geojson
from sentinelsat.sentinel import geojson_to_wkt
from datetime import date

dashes = '=' * 120
#======================================================#
#2. Create Working Directory
#======================================================#
w_dir = os.getcwd()

if os.path.exists(w_dir + '\\' + 'rawdata'):
   shutil.rmtree(w_dir + '\\' + 'rawdata')

if os.path.exists(w_dir + '\\' + 'extracted data'):
   shutil.rmtree(w_dir + '\\' + 'extracted data')

os.mkdir(w_dir + '\\' + 'rawdata')
os.mkdir(w_dir + '\\' + 'extracted data')

#======================================================#
#???
# =====================================================#
#m = folium.Map([-43.32, 171.56], zoom_start = 10)
#boundsdata = 'C:\\Users\\admin\\Documents\\COGS 2020\\Final Project\\aoimap\\map.geojson'
#folium.GeoJson(boundsdata).add_to(m)
#======================================================#
#3. connect to Copernicus Open Access API
#======================================================#
print(dashes)
print('Connecting to Sentinel API')
print(dashes)

api = SentinelAPI('simonirving', 'Yodney1!', 'https://scihub.copernicus.eu/dhus')
#======================================================#
#4. search for desired scene
#======================================================#
footprint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footprint,
                     producttype='SLC',
                     date = ('20200101', '20200111'),
                     orbitdirection='ASCENDING',
                     platformname = 'Sentinel-1'
                     #cloudcoverpercentage=(0, 100)
                     )
lp = len(products)
print(f'A total of { lp } products were found')
#======================================================#
#5. Find desired scene
#======================================================#
print(dashes)
print('\t\t\tUUID\t\t\t\t\t\t\t\t\t\t\t\t\tTitle')
print(dashes)

pd.set_option('display.max_colwidth', None)
products_df = api.to_dataframe(products)
products_df['row_num'] = np.arange(len(products_df))

pro = products_df[['title','size']]

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(products_df.index)
print(dashes)
#======================================================#
#6. Choice to Download files
#======================================================#
while True:
    choice = (input("\nWould You like to Download the data? Y/N  :  "))
    if choice.lower() == 'y':
        api.download_all(products, os.path.join('rawdata'))
        print(dashes)
        print("Begining to Download the data")
        print(dashes)
    else:
        print(dashes)
        print("No data to will be downloaded")
        print(dashes)
        break
