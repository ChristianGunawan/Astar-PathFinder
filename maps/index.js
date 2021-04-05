function initMap() {
    // The location of monas
    const monas = { lat: -6.175252901681506, lng: 106.82713921415032 };
    // The map, centered at monas
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: monas,
    });
    // The marker, positioned at monas
    const marker = new google.maps.Marker({
      position: monas,
      map: map,
    });

    // METHOD

    // ZOOM KETIKA DI CLICK
    map.addListener("center_changed", () => {
      // 3 seconds after the center of the map has changed, pan back to the
      // marker.
      window.setTimeout(() => {
        map.panTo(marker.getPosition());
      }, 3000);
    });

    marker.addListener("click", () => {
      map.setZoom(16);
      map.setCenter(marker.getPosition());
    });


    map.addListener("click", (e) => {
      placeMarkerAndPanTo(e.latLng, map);
    });
  }

  function placeMarkerAndPanTo(latLng, map) {
    new google.maps.Marker({
      position: latLng,
      map: map,
    });
    map.panTo(latLng);
  }