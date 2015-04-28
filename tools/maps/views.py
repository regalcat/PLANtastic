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
def mapsView(request, eventid):
	event = EventModel.getEvent(eventid)
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	if request.method == 'GET':
		gmaps = Gmap.objects.filter(event = event)
		mapform = MapForm()
			

		context = {'menu' : getMenuInfo(request), 'title' : "Edit Maps", \
		  'cur_path' : request.get_full_path(), 'event' : event, 'mapform':mapform,'gmaps':gmaps  }
		return render(request, 'maps/edit.html', context)

	if request.method == 'POST':
		mapid = request.POST['mapid']
		return HttpResponseRedirect(reverse('events:tools:maps:editmaps', kwargs={'eventid':eventid,}))

@login_required(login_url = '/loginRequired/')
def mapsTile(request, eventid):
	event = EventModel.getEvent(eventid)
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	if request.method == 'GET':
		gmaps = Gmap.objects.filter(event = event)
		q=""
		for gmap in gmaps:
			q=gmap.location
		context = {'event' : event, 'gmaps':gmaps }
		return render(request, 'maps/maps.html', context)




@login_required(login_url = '/loginRequired/')
def mapsEditView(request, mapid, eventid):
	event = EventModel.getEvent(eventid)
	
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	if request.method == 'GET':
		gmap = Gmap.objects.filter(event=event, mapid=mapid)

		context = {'menu' : getMenuInfo(request), 'title' : "Edit Map", \
		  'cur_path' : request.get_full_path(), 'event' : event, 'mapform':mapform,'gmap':gmap  }
		return render(request, 'maps/editMap.html', context)

	if request.method == 'POST':
		mapid = request.POST['mapid']
		q=request.POST['location']
		gmap = Gmap.objects.filter(event=event, mapid=mapid)
		gmap.location=q
		gmap.save()
		return HttpResponseRedirect(reverse('events:tools:maps:editMap', kwargs={'eventid':eventid,'mapid':mapid}))


@login_required(login_url = '/loginRequired/')
def addMapView(request, eventid):
	event = EventModel.getEvent(eventid)
	
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	
	if request.method == 'GET':
		mapform=MapForm()

		context = {'menu' : getMenuInfo(request), 'title' : "Add Map", \
		  'cur_path' : request.get_full_path(), 'event' : event, 'mapform':mapform,  }
		return render(request, 'maps/addMap.html', context)

	if request.method == 'POST':
		mapform=MapForm(request.POST)
		
		if mapform.is_valid():
			gmap=Gmap(event=event,location=request.POST['location'])
			gmap.save()
			
		return HttpResponseRedirect(reverse('events:tools:maps:maps', kwargs={'eventid':eventid,}))


