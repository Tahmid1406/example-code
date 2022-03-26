from osgeo import gdal
import glob

files = glob.glob("*.tif")

vrt = gdal.BuildVRT("Dec18.vrt", files)
gdal.Translate("Dec18.tif", vrt)