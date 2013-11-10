# Installing + Working
Installing programs and getting them to work

## Mac OS X
#### Python Site packages
######  GDAL for virtual env
Download GDAL - http://www.kyngchaos.com/software/frameworks
Install GDAL
Go to '/Library/Frameworks/GDAL.framework/Versions/1.10/Python/2.7/site-packages'
cmd + c
Go to 'venv/lib/python2.7/site-packages'
cmd + v

######  Numpy
```
pip install numpy
```
check if it works
```
import numpy
print numpy.__version__
print numpy.__file__
quit()
```


## Windows
#### Python
site packages are under `C:\Python27\Lib\site-packages`

######  GDAL
Download GDAL for Python from [here] (http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal).
Pay attention if your Python is 32bit or 64bit and what version your Python is.
You find that out by typing `python` in the command line.
Set the environment variables.
