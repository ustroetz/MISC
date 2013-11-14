# Installing + Working
Installing programs and getting them to work

## Mac OS X
#### Python Site packages
######  GDAL for virtual env
1. Download [GDAL] (http://www.kyngchaos.com/software/frameworks)
2. Install GDAL
3. Go to `/Library/Frameworks/GDAL.framework/Versions/1.10/Python/2.7/site-packages`
4. cmd + c
5. Go to `venv/lib/python2.7/site-packages`
6. cmd + v

######  Numpy
```
pip install numpy
```


## Windows
#### Python
site packages are under `C:\Python27\Lib\site-packages`

######  GDAL
* Download GDAL for Python from [here] (http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal).
Pay attention if your Python is 32bit or 64bit and what version your Python is.
You find that out by typing `python` in the command line.
* Set the environment variables.

######  GRASS GIS (grass.script)
* Download OSGeo4W installer (32bit if Python is 32bit).
