var yourDateToGo = new Date("March 19, 2022 16:00:00"); //here you're making new Date object

var timing = setInterval( // you're making an interval - a thing, that is updating content after number of miliseconds, that you're writing after comma as second parameter
  function () {

	var currentDate = new Date().getTime(); //same thing as above
	var timeLeft = yourDateToGo - currentDate; //difference between time you set and now in miliseconds

	var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24)); //conversion miliseconds on days 
	if (days < 10) days="0"+days; //if number of days is below 10, programm is writing "0" before 9, that's why you see "09" instead of "9"
	var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)); //conversion miliseconds on hours
	if (hours < 10) hours="0"+hours;
	var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60)); //conversion miliseconds on minutes 
	if (minutes < 10) minutes="0"+minutes;
	var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);//conversion miliseconds on seconds
	if (seconds < 10) seconds="0"+seconds;

	document.getElementById("countdown").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s"; // putting number of days, hours, minutes and seconds in div, 
	//which id is countdown

	if (timeLeft <= 0) {
	  clearInterval(timing);
	  document.getElementById("countdown").innerHTML = "It's over"; //if there's no time left, programm in this 2 lines is clearing interval (nothing is counting now) 
	  //and you see "It's over" instead of time left
	}
  }, 1000);
  
function myCanvas() {
  document.getElementById("myCanvas").style.wordSpacing = "1px";
}

//let hiddenInput = document.getElementById("Google_API");
//let Google_API_value = hiddenInput.value

let map;

function initMap() {
  const locatie = { lat: 50.857589016464054, lng: 4.266740687166337 }
  map = new google.maps.Map(document.getElementById("map"), {
    center: locatie,
    zoom: 14,
  });
	const contentString =
    '<div id="content">' +
    '<h5 id="firstHeading" class="firstHeading">Kattebroek</h5>' +
    '<div id="bodyContent">' +
    "<p>Elegemstraat 160, 1700 Dilbeek</p>" +
    "</div>" +
		'<a href="https://www.google.be/maps/dir///@50.8446589,4.2793976,13z/data=!4m9!4m8!1m0!1m5!1m1!1s0x47c3c12ebb5068ed:0x14353353d517d12f!2m2!1d4.2667432!2d50.8575305!3e0" target="_blank">' +
		'Go!<i class="fas fa-car-alt ml-2></i>' +
		"</a>" +
    "</div>";
		
	const infowindow = new google.maps.InfoWindow({
    content: contentString,
  });
  const marker = new google.maps.Marker({
    position: locatie,
    map,
    title: "Kattebroek",
  });
	
	marker.addListener("click", () => {
    infowindow.open({
      anchor: marker,
      map,
      shouldFocus: false,
    });
  });
}

$(document).ready(function(){
	$('.dropdown-toggle').dropdown()
});
		
