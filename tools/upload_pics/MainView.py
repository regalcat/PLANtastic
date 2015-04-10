from django.shortcuts import render
from django.views.generic import View

from base.helpers import getMenuInfo
from events.models import EventModel

from .models import UploadedPicModel

class MainView(View):
	template_name = "upload_pics/index.html"

	def get(self, request, eventid):
		pics = UploadedPicModel.objects.filter(event_id = eventid)
		return render(request, self.template_name, \
			{'menu' : getMenuInfo(request), 'title' : "Upload Pics Tool", 'pics' : pics})
