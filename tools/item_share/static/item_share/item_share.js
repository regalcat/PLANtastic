function formChanged(amount, item_id) {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
    	document.getElementById("signup_"+item_id).innerHTML =  xhr.responseText;
	};
	xhr.open("post", document.location, true); // change
//	xhr.setRequestHeader("X-CSRFToken", csrf);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	var data = "amount="+amount+"&item_id="+item_id+"&ajax=True";
	xhr.send(data);
}
