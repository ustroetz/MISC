# Installing + Working
Installing programs and getting them to work

## OS X
#### Python Site packages
######  GDAL for virtual env
```
sudo apt-get install build-essential python-all-dev
wget http://download.osgeo.org/gdal/gdal-1.9.0.tar.gz
tar xvfz gdal-1.9.0.tar.gz
cd gdal-1.9.0
./configure --with-python
make
sudo make install
```
######  Imposm
https://gist.github.com/hanleybrand/8611994

#### Ruby
```
brew install rbenv ruby-build
rbenv install 2.1.4
```
Add this to `.bash_profile`
```
eval "$(rbenv init -)"
```

#### Postgres
brew install postgres
brew install postgis

install pgrouting from source




