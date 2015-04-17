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
from tools.weather.models import WeatherModel


from forms import EventForm, HikeForm, DinnerForm, GenericTripForm, GenericGatheringForm

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def new(request):
	if request.method == "GET":
		eventform = EventForm()
		hikeform = HikeForm()
		dinnerform = DinnerForm()
		generictripform = GenericTripForm()
		genericgatheringform = GenericGatheringForm()
		return render(request, 'events/new.html', {'eventform' :eventform, 'hikeform':hikeform,\
			 'dinnerform':dinnerform, 'generictripform':generictripform, \
			'genericgatheringform':genericgatheringform, 'menu' : getMenuInfo(request), 'title' : "New Event"})
	if request.method == "POST":

		eventform = EventForm(request.POST)
		event_Start_Date=request.POST['event_Start_Date_year']+"-"+request.POST['event_Start_Date_month']+"-"+request.POST['event_Start_Date_day']
		eventType= request.POST['eventType']


		
		event = EventModel()
		event.createEvent(name=request.POST['name'], \
			location=request.POST['location'],event_Start_Date=event_Start_Date, \
			eventType=eventType,event_Description=request.POST['event_Description'])

		event.save()

		member = MembershipModel(event=event, user=request.user, status=MembershipModel.CREATOR)
		member.save()
		
		weather = WeatherModel(event = event)
		weather.save()
		

		if (request.POST['eventType'] == u'hike'):

			duration=request.POST['eventDuration']
			distance=request.POST['eventDistance']
			elevation=request.POST['eventElevation']
			
			event_End_Date=request.POST['event_End_Date_year']+"-"+request.POST['event_End_Date_month']+\
				"-"+request.POST['event_End_Date_day']

			if distance == '':
				distance = None
			if elevation == '':
				elevation = None
			if event_End_Date == '--':
				event_End_Date = None
			



			event = HikeEventModel(event.eventid, \
				name=request.POST['name'], location=request.POST['location'], \
				event_Start_Date=event_Start_Date,event_Description=request.POST['event_Description'], \
				event_End_Date=event_End_Date, duration=duration, distance=distance, 					elevation=elevation, difficulty=request.POST['difficulty'], eventType=eventType)
			event.save()


		elif (request.POST['eventType'] == u'otherTrip'):


			event_End_Date=request.POST['event_End_Date_year']+"-"+request.POST['event_End_Date_month']+\
				"-"+request.POST['event_End_Date_day']

			
			if event_End_Date == '--':
				event_End_Date = None

			event = GenericTripModel(event.eventid, \
				name=request.POST['name'], location=request.POST['location'], \
				event_Start_Date=event_Start_Date,event_Description=request.POST['event_Description'], \
				event_End_Date=event_End_Date, eventType=eventType)
			event.save()

		elif (request.POST['eventType'] == u'otherGathering'):

			event_End_Date=request.POST['event_End_Date_year']+"-"+request.POST['event_End_Date_month']+\
				"-"+request.POST['event_End_Date_day']

			if event_End_Date == '--':
				event_End_Date = None

			event = GenericGatheringModel(event.eventid, \
				name=request.POST['name'], location=request.POST['location'], \
				event_Start_Date=event_Start_Date,event_Description=request.POST['event_Description'], 					event_End_Date=event_EndDate, eventType=eventType)
			event.save()


		elif (request.POST['eventType'] == u'dinner'):

			event = DinnerEventModel(event.eventid, \
				name=request.POST['name'], location=request.POST['location'], \
				event_Start_Date=event_Start_Date,event_Description=request.POST['event_Description'], \
				eventType=eventType)
			event.save()

		

		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(event.eventid))
		#return HttpResponseRedirect(reverse('events:eventHome'))
		
	return render(request, 'events/new.html', { 'menu' : getMenuInfo(request), 'title' : "Create Events"})

