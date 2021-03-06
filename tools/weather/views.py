#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from events.models import EventModel
from models import WeatherModel
from base.helpers import getMenuInfo
from base.permissions import memberCheck, isCreator, isCoplanner
from forms import WeatherForm


@login_required(login_url = '/loginRequired/')
def editWeather(request, eventid):
	event = EventModel.getEvent(eventid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

	creator = isCreator(request.user, event)
	coplanner = isCoplanner(request.user, event)
	if creator == False:
		if coplanner == False:
			return render(request, 'events/notPermission.html', \
			{'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	context = {'menu' : getMenuInfo(request), 'title' : "Edit Weather", 'event' : event}
	information = WeatherModel.objects.filter(event = event)

	if request.method == 'GET':
		instance = WeatherModel.objects.filter(event = event)
		if instance.count() == 0:
			weatherform = WeatherForm()
		else:
			weatherform = WeatherForm(instance = instance[0])

		context['weatherform'] = weatherform
		return render(request, 'weather/editWeather.html', context)

	if request.method == 'POST':
		instance = WeatherModel.objects.filter(event = event)
		if instance.count() == 0:
			weatherform = WeatherForm(request.POST)
		else:
			weatherform = WeatherForm(request.POST, instance = instance[0])
	
		if weatherform.is_valid():
			form = weatherform.save(commit=False)
			form.event = event
			form.save()

		return HttpResponseRedirect(reverse('events:tools:weather:editWeather', kwargs={'eventid' : eventid}))


	

@login_required(login_url = '/loginRequired/')
def weatherTile(request, eventid):
	event = EventModel.getEvent(eventid)
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	creator = isCreator(request.user, event)
	coplanner = isCoplanner(request.user, event)
	context={}
	if request.method == 'GET':
		information = WeatherModel.objects.filter(event = event_)
		
		if information.count() == 1:
			context['state'] = information[0].get_state_display
			context['degreeType'] = information[0].degreeType

			city = information[0].city.title()
			new = ""
			for i in range(len(city)):
				if city[i] == " ":
					new = new + "+"
				else:
					new = new + city[i]
			context['city'] = new

		return render(request, 'weather/maps.html', context)


