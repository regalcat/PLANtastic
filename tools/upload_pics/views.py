from django.views.generic.edit import CreateView

from .models import UploadedPicModel
from base.events.models import EventModel

class UploadPicFormView(CreateView):
	template_name = "upload_pics/upload_pic_form.html"
	model = UploadedPicModel
	fields = ['caption', 'file']

	def get(self, request, eventid):
		self.eventid = eventid
		return super(UploadPicFormView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid = eventid
		return super(UploadPicFormView, self).post(self, request)

	def form_valid(self, form):
		print form.instance.caption
		print form.instance.file
		self.success_url = "."
		form.instance.event = EventModel.getEvent(self.eventid)
		form.instance.uploader = self.request.user
		form.save()
		return super(UploadPicFormView, self).form_valid(form)
