function event2(){
		if(document.getElementById("eventType")=='Hike')
			return 'hike();';
		else if(document.getElementById("eventType")=='Dinner')
			return 'dinner();';
		else if(document.getElementById("eventType")=='Other Trip')
			return 'otherTrip();';
		else
			return 'otherGathering();';
}
function startDate(){
	var year= document.getElementById("startYear").value;
	var month= document.getElementById("startMonth").value;
	var day= document.getElementById("startDay").value;
	var hour= document.getElementById("startHour").value;
	var minute= document.getElementById("startMin").value;
	document.getElementById("eventDateStart").value = year+'-'+month+'-'+day+' '+hour+':'+minute;
	
}


function event3(){
	var t = document.getElementsByName("eventType");
	for(var i=0;i<(document.getElementsByName("eventType").length; i++){
		if(t[i].checked){
			if(t[i].value=='Hike')
				//return 'hike();'
				return {{ hikeform.as_p }}
			else if(t[i].value=='Dinner')
				//return 'dinner();'
				return {{ dinnerform.as_p }}
			else if(t[i].value=='Other Trip')
				//return 'otherTrip();'
				return {{ othertripform.as_p }}
			else if(t[i].value=='Other Gathering')
				//return 'otherGathering();'
				return {{ othergatheringform.as_p }}
		}
	}
}


function hike(){
	//open hike options
	document.getElementById("eventDateEnd").style.display="block";
	document.getElementById("eventDateEndLabel").style.display="block";
	document.getElementById("elevation").style.display="block";
	document.getElementById("elevationLabel").style.display="block";
	document.getElementById("difficulty").style.display="block";
	document.getElementById("difficultyLabel").style.display="block";
	document.getElementById("duration").style.display="block";
	document.getElementById("durationLabel").style.display="block";
	document.getElementById("distance").style.display="block";
	document.getElementById("distanceLabel").style.display="block";

	//clear other options
	document.getElementById("vegan").style.display="none";
	document.getElementById("vegetarian").style.display="none";
	document.getElementById("allergies").style.display="none";
	document.getElementById("accommodationsLabel").style.display="none";
	document.getElementById("allergyList").style.display="none";
	document.getElementById("allergyListLabel").style.display="none";
}

function otherTrip(){
	//show other trip options
	document.getElementById("eventDateEnd").style.display="block";
	document.getElementById("eventDateEndLabel").style.display="block";

	//hide other options
	document.getElementById("elevation").style.display="none";
	document.getElementById("elevationLabel").style.display="none";
	document.getElementById("difficulty").style.display="none";
	document.getElementById("difficultyLabel").style.display="none";
	document.getElementById("duration").style.display="none";
	document.getElementById("durationLabel").style.display="none";
	document.getElementById("distance").style.display="none";
	document.getElementById("distanceLabel").style.display="none";

	document.getElementById("vegan").style.display="none";
	document.getElementById("vegetarian").style.display="none";
	document.getElementById("allergies").style.display="none";
	document.getElementById("accommodationsLabel").style.display="none";
	document.getElementById("allergyList").style.display="none";
	document.getElementById("allergyListLabel").style.display="none";
}

function otherGathering(){
	//show other gathering options
	document.getElementById("eventDateEnd").style.display="block";
	document.getElementById("eventDateEndLabel").style.display="block";

	//hide other options
	document.getElementById("elevation").style.display="none";
	document.getElementById("elevationLabel").style.display="none";
	document.getElementById("difficulty").style.display="none";
	document.getElementById("difficultyLabel").style.display="none";
	document.getElementById("duration").style.display="none";
	document.getElementById("durationLabel").style.display="none";
	document.getElementById("distance").style.display="none";
	document.getElementById("distanceLabel").style.display="none";

	document.getElementById("vegan").style.display="none";
	document.getElementById("vegetarian").style.display="none";
	document.getElementById("allergies").style.display="none";
	document.getElementById("accommodationsLabel").style.display="none";
	document.getElementById("allergyList").style.display="none";
	document.getElementById("allergyListLabel").style.display="none";
}

function dinner(){
	//show dinner options
	document.getElementById("vegan").style.display="block";
	document.getElementById("vegetarian").style.display="block";
	document.getElementById("allergies").style.display="block";
	document.getElementById("accommodationsLabel").style.display="block";
	document.getElementById("allergyList").style.display="block";
	document.getElementById("allergyListLabel").style.display="block";

	//hide other options
	document.getElementById("eventDateEnd").style.display="none";
	document.getElementById("eventDateEndLabel").style.display="none";
	document.getElementById("elevation").style.display="none";
	document.getElementById("elevationLabel").style.display="none";
	document.getElementById("difficulty").style.display="none";
	document.getElementById("difficultyLabel").style.display="none";
	document.getElementById("duration").style.display="none";
	document.getElementById("durationLabel").style.display="none";
	document.getElementById("distance").style.display="none";
	document.getElementById("distanceLabel").style.display="none";
	
	
}
