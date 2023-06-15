var form = document.getElementById("report-form");

form.addEventListener("submit", function(event) {
	event.preventDefault();
	var problem = document.getElementById("problem").value;
	var location = document.getElementById("location").value;
	var time = document.getElementById("time").value;
	var userId = document.getElementById("user-id").value;
	alert("Problem: " + problem + "\nLocation: " + location + "\nTime: " + time + "\nUser ID: " + userId);
});
