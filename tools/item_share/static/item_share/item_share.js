function formChanged(amount, item_id, uid, event_id) {
	alert(amount);
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
    	document.getElementById("username").innerHTML =  xhr.responseText;
	};
	xhr.open("post", document.location, true); // change
	var data = "amount="+amount+"&item_id="+item_id+"&uid="+uid+"&event_id="+event_id;
	xhr.send(data);
}
