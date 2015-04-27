from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ForumModel, ThreadModel, PostModel

class CreateThreadView(CreateView):
	template_name = 'forum/create_thread_form.html'
	model = ThreadModel
	fields = ['ttitle', 'pbody']

	def get(self, request, eventid):
		self.forum = ForumModel.forums.filter(event = getEvent(eventid))
		return super(CreateThreadView, self).get(self, request)

	def post(self, request, eventid):
		self.forum = ForumModel.forums.filter(event = getEvent(eventid))
		return super(CreateThreadView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.forum = self.forum
		form.instance.creator = self.request.user
		return super(CreateThreadView, self).form_valid(form)
