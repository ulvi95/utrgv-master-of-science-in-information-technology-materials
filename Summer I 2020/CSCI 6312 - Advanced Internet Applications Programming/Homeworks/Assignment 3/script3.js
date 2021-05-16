function initMap() {
    let lng = document.getElementById("lng").value;
    let lat = document.getElementById("lat").value;
    require(["esri/Map", "esri/views/MapView"], function(Map, MapView) {
        let map = new Map({
            basemap: "topo-vector"
        });
        let view = new MapView({
            container: "viewMapDiv",
            map: map,
            center: [lng, lat], // longitude, latitude
            zoom: 12
        });
    });
}

function showLngLat(result) {
    document.getElementById('lng').value = result.geometry.location.lng();
    document.getElementById('lat').value = result.geometry.location.lat();
    initMap();
}

function getLngLat(callback, address) {
    geocoder = new google.maps.Geocoder();
    if (geocoder) {
        geocoder.geocode({
            'address': address
        }, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                callback(results[0]);
            }
        });
    }
}
//when "Go" button is clicked, call a function to get Lng/Lat info from Google API using geocoder()
document.getElementById("go").addEventListener("click", function() {
    getLngLat(showLngLat, document.getElementById('address').value) /* The last one should be added to refresh the map. It is done after the second click */
});
