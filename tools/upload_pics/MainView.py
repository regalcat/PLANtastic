from django.shortcuts import redirect, render
from django.views.generic import View

import os

from base.helpers import getMenuInfo
from events.models import EventModel
from settings import settings

from .EditPicView import EditPicView
from .models import UploadedPicModel

class MainView(View):
	template_name = "upload_pics/index.html"

	def get(self, request, eventid):
		pics = UploadedPicModel.objects.filter(event_id = eventid)
		return render(request, self.template_name, \
			{'menu' : getMenuInfo(request), 'title' : "Upload Pics Tool", 'pics' : pics})

	def post(self, request, eventid):
		if request.POST['selected'] == 'None':
			return self.get(request, eventid)
		if 'delete' in request.POST:
			UploadedPicModel.objects.get(file=request.POST['selected']).delete()
			os.remove(os.path.join(settings.BASE_DIR,request.POST['selected']))
			return self.get(request, eventid)
		if 'edit' in request.POST:
			pic = UploadedPicModel.objects.get(file=request.POST['selected'])
			return redirect("edit_pic/"+str(pic.id))
