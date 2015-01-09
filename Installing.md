# Installing + Working
Installing programs and getting them to work

## OS X
#### Python Site packages
######  GDAL for virtual env
```
wget http://download.osgeo.org/gdal/gdal-1.9.0.tar.gz
tar xvfz gdal-1.9.0.tar.gz
cd gdal-1.9.0
./configure --with-python
make
make install
```

with libkml
ustoetz: you need the current development version of libkml: https://github.com/google/libkml 
sigq
Title: google/libkml · GitHub (at github.com) 
ustroetz
Okay and what do I do with it? 
← alexbruy has left  
KyleS
ustroetz: build it, then install it somewhere and use --with-libkml=/your/path/to/libkml/installation. 
KyleS
or if you install it to the system (ie /usr/local), --with-libkml should suffice. 

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
```
brew install postgres
brew install postgis
```
install pgrouting from source

lunchy to start and stop
```
gem install lunchy

lunchy start postgres
lunchy stop postgres
```


