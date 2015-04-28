from django.conf.urls import patterns, url



from views import addFriend, executeAddFriend, addFriendQuery, friendListView



urlpatterns = patterns('', 
	url(r'^list/$', friendListView, name='list'),
	url(r'^addFriendQ/$', addFriendQuery, name='addFriendQ'),
	url(r'^(?P<userid>\d+)/addFriend/$', addFriend, name='addFriend'),
	url(r'^(?P<userid>\d+)/executeAdd/$', executeAddFriend, name='executeAdd'),
	
)
