from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from models import FriendList
from events.models import EventModel
from base.helpers import getMenuInfo


from notifications.models import NotificationModel

@login_required(login_url = '/loginRequired/')
def addFriend(request, user):
	user2 = user
	this user=request.user
	friendlist = FriendList.objects.get(user=request.user)
	if request.method == 'GET':
		
		isNotFriend=True
		for user in friendlist:
			if(user == user2):
				isNotFriend=False
				return render(request, 'friends/alreadyFriend.html', {'menu' : getMenuInfo(request), \
				'title' : "Already Friends"})
		context = {'menu' : getMenuInfo(request), 'title' : "Add Friend", 'isNotFriend':isNotFriend,\
		  'cur_path' : request.get_full_path(),  'event' : event,   }
		return render(request, 'friends/add.html', context)

	if request.method == 'POST':
		msg = str(request.user)+" would like to add you as a friend!"
		recipient= user2
		btnText = "Confirm"
		link = ""
		note=NotificationModel()
		note.createNewNotification(user=recipient, text=msg, link=link, btnText=btnText)
		#friendlist.friends.add(user2)
		#friendlist.save()
		return HttpResponseRedirect(reverse('home'))


@login_required(login_url = '/loginRequired/')
def executeAddFriend(request, user):
	user2 = user
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)
	friendlist2 = FriendList.objects.get(user=user2)
		isNotFriend=True
		for user in friendlist:
			if(user == user2):
				isNotFriend=False
				return render(request, 'friends/alreadyFriend.html', {'menu' : getMenuInfo(request), \
				'title' : "Already Friends"})
		for user in friendlist2:
			if(user == request.user):
				isNotFriend=False
				return render(request, 'friends/alreadyFriend.html', {'menu' : getMenuInfo(request), \
				'title' : "Already Friends"})


		friendlist.friends.add(user2)
		friendlist.save()
		friendlist2.friends.add(request.user)
		friendlist2.save()

		msg = str(request.user)+" added you as a friend!"
		recipient = user2
		note=NotificationModel()
		note.createNewNotification(user=recipient, text=msg)
		
		msg = "You are now friends with " + str(user2) + "!"
		recipient = request.user
		note=NotificationModel()
		note.createNewNotification(user=recipient, text=msg)

		context = {'menu' : getMenuInfo(request), 'title' : "Add Friend", 'isNotFriend':isNotFriend,\
		  'cur_path' : request.get_full_path(),  'event' : event,   }
		return render(request, 'friends/add.html', context)


		return HttpResponseRedirect(reverse('notifications'))


@login_required(login_url = '/loginRequired/')
def addFriendQuery(request):
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)

		if request.method == 'GET':
		
		context = {'menu' : getMenuInfo(request), 'title' : "Add Friend", 'isNotFriend':isNotFriend,\
		  'cur_path' : request.get_full_path(),  'event' : event,   }
		return HttpResponseRedirect(reverse('friends:addFriend', kwargs={'user2':user2,}))

	if request.method == 'POST':
		msg = str(request.user)+" would like to add you as a friend!"
		recipient= user2
		btnText = "Confirm"
		link = ""
		note=NotificationModel()
		note.createNewNotification(user=recipient, text=msg, link=link, btnText=btnText)
		#friendlist.friends.add(user2)
		#friendlist.save()
		return HttpResponseRedirect(reverse('home'))
