from osgeo import gdal
import os
# file = gdal.Open("/mnt/c/Users/ASUS/Desktop/Raster/Dec18.tif")

command = "gdal_translate -b 3 -b 2 -b 1 Dec19.tif Dec19_B13.tif"

os.system(command)