function select(index) {
	picture = document.getElementById(index);
	select = document.getElementById("select");
	oldSelectedIndex = select.selectedIndex;
	select.selectedIndex = index;
	deoutline(document.getElementById(oldSelectedIndex));
	outline(picture);
}

deoutline(pic) {

}

outline(pic) {

}
