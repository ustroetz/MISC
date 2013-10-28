#ogr2ogr (only geometry, no attributes)
import ogr
import osmModule

inFile = 'data/standsWGS.shp'
outFile = 'ogr2ogrtest.geojson'
outFileDriver = "GeoJSON"

# Get the input Layer
inDataSource = ogr.Open(inFile, 0)
inLayer = inDataSource.GetLayer()

# Create the output LayerS
outGeoJson = outfile
outDriver = ogr.GetDriverByName(outFileDriver)

# Create the output GeoJSON
outDataSource = outDriver.CreateDataSource(outGeoJson)
outLayer = outDataSource.CreateLayer( outGeoJson, geom_type=ogr.wkbPolygon )

# Get the output Layer's Feature Definition
outLayerDefn = outLayer.GetLayerDefn()

# Add features to the ouput Layer
for inFeature in inLayer:
    # Create output Feature
    outFeature = ogr.Feature(outLayerDefn)

    # Set geometry as centroid
    geom = inFeature.GetGeometryRef()
    outFeature.SetGeometry(geom)
    # Add new feature to output Layer
    outLayer.CreateFeature(outFeature)

# Close DataSources
inDataSource.Destroy()
outDataSource.Destroy()
