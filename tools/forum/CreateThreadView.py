from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ForumModel, ThreadModel, PostModel

from events.models import EventModel

class CreateThreadView(CreateView):
	template_name = 'forum/create_thread_form.html'
	model = ThreadModel
	fields = ['title', 'body']

	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		self.forum = ForumModel.forums.filter(event = EventModel.getEvent(eventid))
		if self.forum.count() == 0:
			self.forum = ForumModel(event_id = eventid, title=event.name)
			self.forum.save()
		else:
			self.forum = self.forum[0]
		return super(CreateThreadView, self).get(self, request)

	def post(self, request, eventid):
		self.forum = ForumModel.forums.get(event = EventModel.getEvent(eventid))
		return super(CreateThreadView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.forum = self.forum
		form.instance.creator = self.request.user
		return super(CreateThreadView, self).form_valid(form)
