import os
from osgeo import gdal
from osgeo import gdalconst

width = 36141
height = 28197
tilesize = 256

for i in range(0, width, tilesize):
    for j in range(0, height, tilesize):
        gdaltranString = "gdal_translate -of GTIFF -srcwin "+str(i)+", "+str(j)+", "+str(tilesize)+", " \
            +str(tilesize)+" Dec19_B13.tif utm_"+str(i)+"_"+str(j)+".tif"
        os.system(gdaltranString)