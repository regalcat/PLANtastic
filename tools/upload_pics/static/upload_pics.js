function select(index) {
	picture = document.getElementById(index);
	selectObj = document.getElementById("select");
	oldSelectedIndex = selectObj.selectedIndex;
	selectObj.selectedIndex = index;
	deoutline(document.getElementById(oldSelectedIndex));
	outline(picture);
}

function deoutline(pic) {
	// Needed because "None" option does not have an associated element.
	if (pic != null) {
		pic.style.border = "0px solid #000000";
	}
}

function outline(pic) {
	pic.style.border = "thick solid #5555FF";
}
