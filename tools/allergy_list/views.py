#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from tools.allergy_list.models import AllergyModel
from events.models import EventModel
from base.helpers import getMenuInfo
from base.permissions import memberCheck
from forms import AllergyForm

@login_required(login_url = '/loginRequired/')
def allergyindex(request, eventid):
	event = EventModel.getEvent(eventid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')

	persons = AllergyModel.objects.filter(event = event)
	
	context = {'menu' : getMenuInfo(request), 'title' : "Allergy List", 'list' : persons, 'event' : event }
	return render(request, 'allergy_list/allergyIndex.html', context)

@login_required(login_url = '/loginRequired/')
def addAllergy(request, eventid):
	event = EventModel.getEvent(eventid)
	user = request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')
	if request.method == 'GET':
		instance = AllergyModel.objects.filter(event = event, user = user)
		if instance.count() == 0:
			allergyform = AllergyForm()
		else:
			allergyform = AllergyForm(instance = instance[0])

		context = {'menu' : getMenuInfo(request), 'title' : "Add allergies", 'allergyform' : allergyform, 'event' : event, 'user' : request.user}
		return render(request, 'allergy_list/addAllergy.html', context)

	if request.method == 'POST':
		instance = AllergyModel.objects.filter(event = event, user = user)
		if instance.count() == 0:
			allergyform = AllergyForm(request.POST)
		else:
			allergyform = AllergyForm(request.POST, instance = instance[0])

		
		if allergyform.is_valid():
			form = allergyform.save(commit=False)
			form.user = request.user
			form.event = event
			form.save()
		return HttpResponseRedirect(reverse('events:tools:allergylist:addAllergy', kwargs={'eventid' : eventid}))

	
	
