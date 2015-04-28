from django.conf.urls import patterns, url

from .RideShareView import RideShareView

from views import addFriend, executeAddFriend, addFriendQuery, friendListView, leaveCar, executeLeaveCar, declineFriend



urlpatterns = patterns('', 
	url(r'^$', friendListView, name='list'),
	url(r'^addFriendQ/$', addFriendQuery, name='addFriendQ'),
	url(r'^(?P<userid>\d+)/addFriend/$', addFriend, name='addFriend'),
	url(r'^(?P<userid>\d+)/executeAdd/$', executeAddFriend, name='executeAdd'),
	url(r'^(?P<userid>\d+)/declineFriend/$', declineFriend, name="declineFriend"),
	
)
