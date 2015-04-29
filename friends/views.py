from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import FriendList
from events.models import EventModel
from base.helpers import getMenuInfo
from forms import AddFriendForm


from notifications.models import NotificationModel

@login_required(login_url = '/loginRequired/')
def addFriend(request, userid):
	user2 = User.objects.get(id=userid)
	thisUser=request.user
	friendlist = FriendList.objects.filter(user=request.user)
	
		
	isNotFriend=True
	for user in friendlist[0].friends.all():
		if(user == user2):
			isNotFriend=False
			return render(request, 'friends/alreadyFriend.html', {'menu' : getMenuInfo(request), \
			'title' : "Already Friends"})
	
	context = {'menu' : getMenuInfo(request), 'title' : "Add Friend", 'isNotFriend':isNotFriend,\
	  'cur_path' : request.get_full_path(),    }

	msg = str(request.user)+" would like to add you as a friend!"
	recipient= user2
	btnText = "Confirm"
	link = "friends:executeAdd"
	friendarg = thisUser.id
	note=NotificationModel()
	note.createButtonNotification(user=recipient, text=msg, link=link, btnText=btnText, friendarg=friendarg, eventarg=None)
	
	return HttpResponseRedirect(reverse('friends:list'))


@login_required(login_url = '/loginRequired/')
def executeAddFriend(request, userid):
	user2 = User.objects.get(id=userid)
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)
	friendlist2 = FriendList.objects.get(user=user2)
	isNotFriend=True
	for user in friendlist.friends.all():
		if(user == user2):
			isNotFriend=False
			return render(request, 'friends/alreadyFriend.html', {'menu' : getMenuInfo(request), \
				'title' : "Already Friends"})
	for user in friendlist2.friends.all():
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

	
	return HttpResponseRedirect(reverse('friends:list'))


@login_required(login_url = '/loginRequired/')
def declineFriend(request, userid):
	
	note = NotificationModel.objects.filter(user = request.user, friendarg=userid)
	if note.count() == 1:
		note.delete()

	return HttpResponseRedirect(reverse("notifications:notifications.index"))
	


@login_required(login_url = '/loginRequired/')
def addFriendQuery(request):
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)
	addfriendform = AddFriendForm()
	if request.method == 'GET':
		
		context = {'menu' : getMenuInfo(request), 'title' : "Add Friend", \
		  'cur_path' : request.get_full_path(),  'addfriendform':addfriendform }
		return render(request, 'friends/addFriend.html', context)

	if request.method == 'POST':

		friend = request.POST['friend']
		user2 = User.objects.filter(username=friend)
		if(user2[0] == request.user):
			return HttpResponseRedirect("")
		if user2.count() != 1:
			return HttpResponseRedirect(reverse("friends:addFriendQ"))
		
		user2 = User.objects.get(username=friend)
		msg = "You sent a friend request to " + str(user2)+"."
		recipient = request.user
		note=NotificationModel()
		note.createNewNotification(user=recipient, text=msg)
		return HttpResponseRedirect(reverse('friends:addFriend', kwargs={'userid':int(user2.id)}))


@login_required(login_url = '/loginRequired/')
def friendListView(request):
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)
	if request.method == 'GET':

		context = {'menu' : getMenuInfo(request), 'title' : "Friends", 'friendlist':friendlist,\
		  'cur_path' : request.get_full_path(),  }
		return render(request, 'friends/friendList.html', context)


@login_required(login_url = '/loginRequired/')
def deleteFriend(request, userid):
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)
	friend = User.objects.get(id=userid)
	if request.method == 'GET':
		
		context = {'menu' : getMenuInfo(request), 'title' : "Delete Friend", 'friend':friend,\
		  'cur_path' : request.get_full_path(),  }
		return render(request, 'friends/deleteFriend.html', context)
	if request.method == 'POST':

		return HttpResponseRedirect(reverse('friends:executeDelete', kwargs={'userid':userid}))




@login_required(login_url = '/loginRequired/')
def executeDeleteFriend(request, userid):
	user2 = User.objects.get(id=userid)
	thisUser=request.user
	friendlist = FriendList.objects.get(user=request.user)
	friendlist2 = FriendList.objects.get(user=user2)
	isNotFriend=True
	for user in friendlist.friends.all():
		if(user == user2):
			isNotFriend=False
	for user in friendlist2.friends.all():
		if(user == request.user):
			isNotFriend=False
	if isNotFriend:	
		return HttpResponseRedirect("")


	friendlist.friends.remove(user2)
	friendlist.save()
	friendlist2.friends.remove(request.user)
	friendlist2.save()
	
	msg = "You removed " + str(user2) + " from your friends list"
	recipient = request.user
	note=NotificationModel()
	note.createNewNotification(user=recipient, text=msg)

	
	return HttpResponseRedirect(reverse('friends:list'))



