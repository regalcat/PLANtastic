#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from notifications.models import NotificationModel
from base.helpers import getMenuInfo


@login_required(login_url = '/loginRequired/')
def notifications(request):

	notifications = NotificationModel.objects.filter(user = request.user).order_by("-time")
	i = 0

	for note in notifications:
		if i > 25 and note.seen == True:
			note.delete()
			i += 1
			continue

		if note.seen == False:
			note.seen = True
			note.save()
		i += 1

	context = {'menu' : getMenuInfo(request), 'title' : "Notifications", 'notifications' : notifications}

	return render(request, 'notifications/notifications.html', context)
