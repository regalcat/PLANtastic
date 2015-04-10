
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView



from models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel
from invite.models import InviteModel, MembershipModel
from base.helpers import getMenuInfo


from forms import EventForm, HikeForm, DinnerForm, GenericTripForm, GenericGatheringForm



@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def new(request):
	if request.method == "GET":
		eventform = EventForm()
		
		return render(request, 'events/new.html', {'eventform' :eventform, 'menu' : getMenuInfo(request), 'title' : "New Event"})
	if request.method == "POST":

		eventform = EventForm(request.POST)
		event = EventModel()
		eventDateStart=request.POST['eventDateStart_year']+"-"+request.POST['eventDateStart_month']+"-"+request.POST['eventDateStart_day']
		eventType= request.POST['eventType']
		event.createEvent(eventName=request.POST['eventName'],eventLocation=request.POST['eventLocation'],eventDateStart=eventDateStart,eventType=eventType,eventDescription=request.POST['eventDescription'])
		event.save()
		member = MembershipModel(event=event, user=request.user, status=MembershipModel.CREATOR)
		member.save()
		if not eventform.is_valid():
			#eventform.save()
			#return render(request, 'events/eventHome/'+str(event.eventid))
			return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(event.eventid))	
			#return HttpResponseRedirect(reverse('events:eventHome'))
		
		

		

		if (request.POST['eventType'] == u'hike'):
			eventDuration=request.POST['eventDuration']
			eventDistance=request.POST['eventDistance']
			eventElevation=request.POST['eventElevation']
			eventDateEnd=request.POST['eventDateEnd']

			if eventDistance == '':
				eventDistance = None
			if eventElevation == '':
				eventElevation = None
			if eventDateEnd == '':
				eventDateEnd = None
			
			event = HikeEventModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=eventDateStart,eventDescription=request.POST['eventDescription'], \
				eventDateEnd=eventDateEnd, eventDuration=eventDuration, eventDistance=eventDistance, 					eventElevation=eventElevation, eventDifficulty=request.POST['difficulty'])
			event.save()

		if (request.POST['eventType'] == u'otherTrip'):
			eventDateEnd=request.POST['eventDateEnd']
			if eventDateEnd == '':
				eventDateEnd = None

			event = GenericTripModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=eventDateStart,eventDescription=request.POST['eventDescription'], 					eventDateEnd=eventDateEnd)
			event.save()

		if (request.POST['eventType'] == u'otherGathering'):
			eventDateEnd=request.POST['eventDateEnd']
			if eventDateEnd == '':
				eventDateEnd = None

			event = GenericGatheringModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=eventDateStart,eventDescription=request.POST['eventDescription'], 					eventDateEnd=eventDateEnd)
			event.save()

		if (request.POST['eventType'] == u'dinner'):

			event = DinnerEventModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=eventDateStart,eventDescription=request.POST['eventDescription'])
			event.save()

		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(event.eventid))
		#return HttpResponseRedirect(reverse('events:eventHome'))
		
	return render(request, 'events/new.html', { 'menu' : getMenuInfo(request), 'title' : "Create Events"})

