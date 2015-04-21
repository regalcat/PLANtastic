#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from tools.schedule.models import ScheduleModel
from events.models import EventModel
from base.helpers import getMenuInfo
from base.permissions import memberCheck
from tools.schedule.forms import ScheduleForm


@login_required(login_url = '/loginRequired/')
def showSchedule(request, eventid):
	event = EventModel.getEvent(eventid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

	activities = ScheduleModel.objects.filter(event = event).order_by("start_date")

	context = {'menu' : getMenuInfo(request), 'title' : "Schedule", 'activities' : activities, 'event': event}

	return render(request, 'schedule/showSchedule.html', context)



@login_required(login_url = '/loginRequired/')
def editActivity(request, eventid):

	scheduleid = request.GET['scheduleid']
	event = EventModel.getEvent(eventid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')


	if request.method == 'GET':
		instance = ScheduleModel.objects.filter(scheduleid = scheduleid)
		if instance.count() == 0:
			scheduleform = ScheduleForm()
		else:
			scheduleform = ScheduleForm(instance = instance[0])

		context = {'menu' : getMenuInfo(request), 'title' : "Edit schedule", 'scheduleform' : scheduleform, 'event' : event}
		return render(request, 'schedule/editActivity.html', context)


	if request.method == 'POST':
		instance = ScheduleModel.objects.filter(event = event)
		if instance.count() == 0:
			scheduleform = ScheduleForm(request.POST)
		else:
			scheduleform = ScheduleForm(request.POST, instance = instance[0])

		if scheduleform.is_valid():
			form = scheduleform.save(commit=False)
			form.event = event
			form.scheduleid = scheduleid

			start_date=request.POST['start_date_year']+"-"+request.POST['start_date_month']+"-"+ \
			request.POST['start_date_day']+" "+request.POST['start_hour']+":"+request.POST['start_minute']

			end_date=request.POST['end_date_year']+"-"+request.POST['end_date_month']+"-"+ \
			request.POST['end_date_day']+" "+request.POST['end_hour']+":"+request.POST['end_minute']

			if end_date == "0-0-0 0:0":
				end_date = None
		
			form.start_date = start_date
			form.end_date = end_date
			form.save()

			return HttpResponseRedirect("")

	



@login_required(login_url = '/loginRequired/')
def addActivity(request, eventid):
	event = EventModel.getEvent(eventid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')


	if request.method == 'GET':
		scheduleform = ScheduleForm()

		context = {'menu' : getMenuInfo(request), 'title' : "Edit schedule", \
		'scheduleform' : scheduleform, 'event' : event}
		return render(request, 'schedule/newActivity.html', context)


	if request.method == 'POST':
		scheduleform = ScheduleForm(request.POST)
		
		activity = ScheduleModel()

		start_date=request.POST['start_date_year']+"-"+request.POST['start_date_month']+"-"+request.POST['start_date_day']+" "+request.POST['start_hour']+":"+request.POST['start_minute']

		end_date=request.POST['end_date_year']+"-"+request.POST['end_date_month']+"-"+request.POST['end_date_day']+" "+request.POST['end_hour']+":"+request.POST['end_minute']
		

		if end_date == "0-0-0 0:0":
			end_date = None


		activity.createActivity(event, name=request.POST['name'],description=request.POST['description'], start_date=start_date, end_date=end_date)
		activity.save()
		
		
		return HttpResponseRedirect("")



