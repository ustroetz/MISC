## Documentation

###### Python GDAL
http://pcjericks.github.io/py-gdalogr-cookbook/<br>
http://www.gis.usu.edu/~chrisg/python/2009/
http://gdal.org/python/

## Version 

###### Python
```
$ python --version
```

###### Numpy
```
>>>import numpy
>>>numpy.__version__
```

###### GDAL Python is using
```
>>>import gdal
>>>gdal.VersionInfo()
```

###### GDAL command line
```
$ gdalinfo --version
````
###### GDAL easy_install installed
```
$ easy_install GDAL
```

## Python site packages
###### Installed site packages
```
$ pip freeze
```

## Location
###### Location of Python
```
$ which python
````

###### Location of Python site packages
````
$ python -m site --user-site
````
```
>>>import site
>>>site.getsitepackages()
````

###### Location of Numpy Python is using
```
>>>import numpy
>>>numpy.__file__
````

## Path Variable
###### Show Path Variable
```
$ echo $PATH
```
