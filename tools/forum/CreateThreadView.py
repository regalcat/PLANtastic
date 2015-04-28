from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ForumModel, ThreadModel, PostModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from events.models import EventModel
from base.permissions import memberCheck

class CreateThreadView(CreateView):
	template_name = 'forum/create_thread_form.html'
	model = ThreadModel
	fields = ['title', 'body']

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		event = EventModel.getEvent(eventid)
		self.forum = ForumModel.forums.filter(event = EventModel.getEvent(eventid))
		if self.forum.count() == 0:
			self.forum = ForumModel(event_id = eventid, title=event.name)
			self.forum.save()
		else:
			self.forum = self.forum[0]
		return super(CreateThreadView, self).get(self, request)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		self.forum = ForumModel.forums.get(event = EventModel.getEvent(eventid))
		return super(CreateThreadView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../../../"
		form.instance.forum = self.forum
		form.instance.creator = self.request.user
		return super(CreateThreadView, self).form_valid(form)
