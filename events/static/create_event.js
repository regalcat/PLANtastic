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
	var i =0;
	for(i=0; i<document.getElementsByName("eventType").length; i++){
		if(t[i].checked){
			if(t[i].value=='Hike')
				return 'hike();'
				//hikeform.as_p()
			else if(t[i].value=='Dinner')
				return 'dinner();'
				//dinnerform.as_p()
			else if(t[i].value=='Other Trip')
				return 'otherTrip();'
				//othertripform.as_p()
			else if(t[i].value=='Other Gathering')
				return 'otherGathering();'
				//othergatheringform.as_p()
		}
	}
}


function hike(){
	//open hike options
	document.getElementById("event_End_Date").style.display="inline";
	document.getElementById("event_End_Date_day").style.display="inline";
	document.getElementById("event_End_Date_month").style.display="inline";
	document.getElementById("event_End_Date_year").style.display="inline";
	document.getElementById("elevation").style.display="inline";
	document.getElementById("elevationLabel").style.display="inline";
	document.getElementById("difficulty").style.display="inline";
	document.getElementById("difficultyLabel").style.display="inline";
	document.getElementById("duration").style.display="inline";
	document.getElementById("durationLabel").style.display="inline";
	document.getElementById("distance").style.display="inline";
	document.getElementById("distanceLabel").style.display="inline";

}

function otherTrip(){
	//show other trip options
	document.getElementById("event_End_Date").style.display="inline";
	document.getElementById("event_End_Date_day").style.display="inline";
	document.getElementById("event_End_Date_month").style.display="inline";
	document.getElementById("event_End_Date_year").style.display="inline";

	//hide other options
	document.getElementById("elevation").style.display="none";
	document.getElementById("elevationLabel").style.display="none";
	document.getElementById("difficulty").style.display="none";
	document.getElementById("difficultyLabel").style.display="none";
	document.getElementById("duration").style.display="none";
	document.getElementById("durationLabel").style.display="none";
	document.getElementById("distance").style.display="none";
	document.getElementById("distanceLabel").style.display="none";

}

function otherGathering(){
	//show other gathering options
	document.getElementById("event_End_Date").style.display="inline";
	document.getElementById("event_End_Date_day").style.display="inline";
	document.getElementById("event_End_Date_month").style.display="inline";
	document.getElementById("event_End_Date_year").style.display="inline";
	//hide other options
	document.getElementById("elevation").style.display="none";
	document.getElementById("elevationLabel").style.display="none";
	document.getElementById("difficulty").style.display="none";
	document.getElementById("difficultyLabel").style.display="none";
	document.getElementById("duration").style.display="none";
	document.getElementById("durationLabel").style.display="none";
	document.getElementById("distance").style.display="none";
	document.getElementById("distanceLabel").style.display="none";

}

function dinner(){
	

	//hide other options

	document.getElementById("elevation").style.display="none";
	document.getElementById("elevationLabel").style.display="none";
	document.getElementById("difficulty").style.display="none";
	document.getElementById("difficultyLabel").style.display="none";
	document.getElementById("duration").style.display="none";
	document.getElementById("durationLabel").style.display="none";
	document.getElementById("distance").style.display="none";
	document.getElementById("distanceLabel").style.display="none";

	document.getElementById("event_End_Date").style.display="none";
	document.getElementById("event_End_Date_day").style.display="none";
	document.getElementById("event_End_Date_month").style.display="none";
	document.getElementById("event_End_Date_year").style.display="none";
	
	
}
