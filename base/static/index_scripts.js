var pics = null;

(function setup() {
	document.body.style.height = "" + window.innerHeight + "px"
	document.body.style.backgroundSize = "contain"
	document.body.style.backgroundRepeat = 'no-repeat';
	document.body.style.backgroundPosition = "center";
})()


function changeBackground() {
	var n = Math.floor((Math.random()*pics.pics.length));
	var image = pics.pics[n];
	var temp = "url('" + image + "')";
	document.body.style.backgroundImage = temp;
}

(function getBackgroundPics() {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (xhr.readyState == xhr.DONE) {
			pics = JSON.parse(xhr.responseText);
			changeBackground();
			window.setInterval(changeBackground, 30000);
		}
	}
	xhr.open("get", "cover-pic/", true);
	xhr.send(null);
})()
