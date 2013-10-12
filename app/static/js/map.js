var map;
var mapCenter=new google.maps.LatLng(51.508742,-0.120850);

function initialize()
{
var mapStruct = {
  center:mapCenter,
  zoom:3, //0(world) - 21(creeper)
  mapTypeId:google.maps.MapTypeId.HYBRID //other options:ROADMAP, SATELLITE, HYBRID,TERRAIN
  };

  map = new google.maps.Map(document.getElementById("googleMap"),mapStruct);

  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng);
    getPictures(event.latLng);
    alert('Lat: ' + event.latLng.lat() + ' and Longitude is: ' + event.latLng.lng());
  });
}

function placeMarker(location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map,
  });
  var infowindow = new google.maps.InfoWindow({
    content: 'Latitude: ' + location.lat() + '<br>Longitude: ' + location.lng()
  });
  infowindow.open(map,marker);
}

function getPictures(location){

}

google.maps.event.addDomListener(window, 'load', initialize);