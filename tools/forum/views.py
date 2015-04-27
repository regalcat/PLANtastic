from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from base.helpers import getMenuInfo
from events.models import EventModel
from tools.forum.models import ForumModel, ThreadModel, PostModel
from tools.ToolView import ToolView

class ForumView(ToolView):
	tile_template = "forum/forumTemplate.html"

	@staticmethod
	def getIdentifier():
		return "forum"
	
	#returns the number of posts in the given thread
	def numPosts(cur_thread):
		num = len(PostModel.posts.filter(thread = cur_thread))
		return num

	def getContext():
		
		return context

	#Returns the template for the forum tile in the event page
	
	def get(self, request, eventid):
		user = request.user
		cur_event = EventModel.getEvent(eventid)
		cur_forum = ForumModel.forums.filter(event=cur_event)
		threads = ThreadModel.threads.filter(forum=cur_forum)
		template = loader.get_template("forum/forumTemplate.html")
		context = RequestContext(request, {'threads' : threads, 'event' : cur_event, 'cur_path' : request.get_full_path(), 'title' : forum.title, 'menu' : getMenuInfo(request) })
		return HttpResponse(template.render(context))

	#Adds the new thread and the initial post and returns the get view
	
	def post(self, request, eventid):
		cur_event = getEvent(eventid)
		ttitle = request.POST['ttitle']
		tforum = ForumModel.forums.filter(event = cur_event)
		tcreator = request.user
		thread = ThreadModel(title=ttitle, creator=tcreator, forum=tforum)
		thread.save()
		pbody = request.POST['pbody']
		post = PostModel(title=ttitle, creator=tcreator, thread=thread, body=pbody)
		post.save()
		return self.get(request, eventid)

class ThreadView(View):
	template = "forum/threadTemplate.html"
	
	#Gets a paginated list of the posts in the current thread
	
	def get(self, request, eventid, key):
		cur_event = EventModel.getEvent(eventid)
		posts = Post.posts.filter(thread=key).order_by("created")
		title = ThreadModel.threads.get(pk=key).title
		context = RequestContext(request, {'posts' : posts, 'thread' : ThreadModel.threads.get(pk=key), 'event' : cur_event, 'cur_path' : request.get_full_path(), 'title' : title, 'menu' : getMenuInfo(request) })
		return HttpResponse(template.render(context))
	
	#Adds the post to the thread and returns the get method
	
	def post(self, request, eventid, key):
		cur_event = EventModel.getEvent(eventid)
		cur_thread = ThreadModel.threads.get(pk=key)
		puser = request.user
		ptitle = request.POST['ptitle']
		pbody = request.POST['pbody']
		post = PostModel(title=ptitle, creator=puser, thread=cur_thread, body=pbody)
		post.save()
		return self.get(request, eventid)
