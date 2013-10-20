var map = new OpenLayers.Map('map', {
    controls: [new OpenLayers.Control.Navigation()] // removes default controls
});
var layerOSM = new OpenLayers.Layer.OSM( "Simple OSM Map");
var vector = new OpenLayers.Layer.Vector('vector');


// find users location
var geolocate = new OpenLayers.Control.Geolocate();
map.addControl(geolocate);
geolocate.events.register("locationupdated",geolocate,function(e) {
    var circle = new OpenLayers.Feature.Vector(
        OpenLayers.Geometry.Polygon.createRegularPolygon(
            new OpenLayers.Geometry.Point(e.point.x, e.point.y),
            e.position.coords.accuracy,
            40,
            0
        )
    );
    vector.addFeatures([circle]);
    map.zoomToExtent(vector.getDataExtent());	
});
geolocate.activate();


//Create layer that queries bike racks from overpass api
var layerBikeRack = new OpenLayers.Layer.Vector("Point", {
    strategies: [new OpenLayers.Strategy.Fixed()],
    protocol: new OpenLayers.Protocol.HTTP({
        url: "http://www.overpass-api.de/api/xapi?node[bbox=-122.9130,45.4066,-122.3946,45.6788][amenity=bicycle_parking]",
        format: new OpenLayers.Format.OSM()
    }),
});

// add layers to map
map.addLayers([layerOSM]);
map.addLayers([layerBikeRack]);

// NEEDS WORK: get bounding box of user area and pass it into the url
// console.log(OpenLayers.Feature.Geometry.getBounds);
