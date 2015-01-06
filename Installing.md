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
rbenv install -l     # list available ruby versions
rbenv install 2.1.2  # install the ruby you want
rbenv global 2.1.2   # set it as the default
```
Add this add bottom of `.bash_profile`
```
eval "$(rbenv init -)"
```
cannot live without bundle
```
gem install bundler
rbenv rehash
```

#### Postgres
brew install postgres
brew install postgis

install pgrouting from source




