function formChanged(amount, item_id, uid, event_id, csrf) {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
    	document.getElementById("username").innerHTML =  xhr.responseText;
	};
	xhr.open("post", document.location, true); // change
	xhr.setRequestHeader("X-CSRFToken", csrf);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	var data = "amount="+amount+"&item_id="+item_id+"&event_id="+event_id;
	xhr.send(data);
}
