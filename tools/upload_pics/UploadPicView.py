from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import UploadedPicModel
from events.models import EventModel
from base.permissions import memberCheck

class UploadPicFormView(CreateView):
	template_name = "upload_pics/upload_pic_form.html"
	model = UploadedPicModel
	fields = ['title', 'caption', 'file']

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
		self.eventid = eventid
		return super(UploadPicFormView, self).get(self, request)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
		self.eventid = eventid
		#TODO - error checking on uploads
		super(UploadPicFormView, self).post(self, request)
		return HttpResponseRedirect("../")

	def form_valid(self, form):
		print form.instance.caption
		print form.instance.file
		self.success_url = "."
		form.instance.event = EventModel.getEvent(self.eventid)
		form.instance.uploader = self.request.user
		form.save()
		return super(UploadPicFormView, self).form_valid(form)
