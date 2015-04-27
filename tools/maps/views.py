from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from tools.maps.models import *
from events.models import EventModel
from base.helpers import getMenuInfo
from base.permissions import memberCheck
from forms import MapForm
from notifications.models import NotificationModel


@login_required(login_url = '/loginRequired/')
def mapsEditView(request, eventid):
	event = EventModel.getEvent(eventid)
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	if request.method == 'GET':
		gmaps = Gmap.objects.filter(event = event)

			

		context = {'menu' : getMenuInfo(request), 'title' : "Edit Maps", \
		  'cur_path' : request.get_full_path(), 'event' : event, 'gmaps':gmaps  }
		return render(request, 'maps/edit.html', context)

	if request.method == 'POST':
		mapid = request.POST['mapid']
		return HttpResponseRedirect(reverse('events:tools:maps:edit', kwargs={'eventid':eventid,}))

@login_required(login_url = '/loginRequired/')
def mapsTile(request, eventid):
	event = EventModel.getEvent(eventid)
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	if request.method == 'GET':
		gmaps = Gmap.objects.filter(event = event)
		
		context = {'event' : event, 'gmaps':gmaps }
		return render(request, 'maps/maps.html', context)

	if request.method == 'POST':
		mapid = request.POST['mapid']
		return HttpResponseRedirect(reverse('events:tools:maps:edit', kwargs={'eventid':eventid,}))


