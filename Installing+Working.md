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
* Set Enviroment Variables
    * set GISBASE=C:\OSGeo4W\apps\grass\grass-6.4.3
    * set GISRC=C:\Users\<username>\AppData\Roaming\GRASS6\.grassrc6
    * set LD_LIBRARY_PATH=C:\OSGeo4W\apps\grass\grass-6.4.3\lib
    * set PYTHONLIB=C:\Python27
    * set PYTHONPATH=C:\OSGeo4W\apps\grass\grass-6.4.3\etc\python
    * set GRASS_SH=C:\OSGeo4W\apps\msys\bin\sh.exe
    * set PATH=C:\OSGeo4W\apps\grass\grass-6.4.3\etc;
               C:\OSGeo4W\apps\grass\grass-6.4.3\etc\python;
               C:\OSGeo4W\apps\grass\grass-6.4.3\lib;
               C:\OSGeo4W\apps\grass\grass-6.4.3\bin;
               C:\OSGeo4W\apps\msys\bin;
               C:\Python27
python
