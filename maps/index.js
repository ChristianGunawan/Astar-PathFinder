function initMap() {
    // The location of monas
    const monas = { lat: -6.175252901681506, lng: 106.82713921415032 };
    // The map, centered at monas
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 17,
      center: monas,
    });
    // The marker, positioned at monas
    const marker = new google.maps.Marker({
      position: monas,
      map: map,
    });
  }