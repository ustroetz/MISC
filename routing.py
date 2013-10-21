# determines the distance from points in a shapefile to the destination specified in as a attribute in the shapfile
import requests
import ogr

def routing(start,stop):

    headers = {'User-Agent': 'Forestry Scenario Planner'}
    url = 'http://router.project-osrm.org/viaroute?loc=' + start + '&loc=' + stop
    response = requests.get(url, headers=headers)
    data = response.json()

    # parse json string for distance
    total_summary = data['route_summary']
    total_distance = total_summary['total_distance']  # in meters

    return total_distance

def distance(shapefile,fieldDestLon,fieldDestLat,fieldDist):
    driver = ogr.GetDriverByName('ESRI Shapefile')
    fn = shapefile
    dataSource = driver.Open(fn, 1)
    layer = dataSource.GetLayer()
    feature = layer.GetNextFeature()
    while feature:
        destLon = feature.GetFieldAsDouble('destLon')
        destLat = feature.GetFieldAsDouble('destLat')
        geometry = feature.GetGeometryRef()
        x = geometry.GetX()
        y = geometry.GetY()
        start = '%f,%f' % (y,x)
        stop = '%f,%f' % (destLat,destLon)
        dist = routing(start,stop) # returns distance in meters
        dist = dist/1000.0
        feature.SetField(fieldDist, dist)
        layer.SetFeature(feature)
        feature = layer.GetNextFeature()
    dataSource.Destroy()


# test
shapefile = 'dist.shp' # shapefile containing the points
fieldDestLon = 'destLon' # field name longitude of destination
fieldDestLat = 'destLat' # field name latitude of destination
fieldDist = 'dist' # field name where the destination will be stored in 
distance(shapefile,fieldDestLon,fieldDestLat,fieldDist)
