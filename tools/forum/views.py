from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from base.helpers import getMenuInfo
from events.models import EventModel
from tools.forum.models import ForumModel, ThreadModel, PostModel
from tools.ToolView import ToolView

class ForumView(ToolView):
	template = "forum/forumTemplate.html"

	@staticmethod
	def getIdentifier():
		return "forum"
	
	def get(self, request, eventid):
		user = request.user
		cur_event = EventModel.getEvent(eventid)
		cur_forum = ForumModel.forums.filter(event=cur_event)
		threads = ThreadModel.threads.filter(forum=cur_forum)
		template = loader.get_template("forum/forumTemplate.html")
		context = RequestContext(request, {'threads' : threads, 'event' : cur_event, 'cur_path' : request.get_full_path(), 'title' : forum.title, 'menu' : getMenuInfo(request) })
		return HttpResponse(template.render(context))

	def post(self, request, eventid):
		cur_event = getEvent(eventid)
		#TODO - Add the new thread to the forum
		return self.get(request, eventid)

