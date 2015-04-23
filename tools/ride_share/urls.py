from django.conf.urls import patterns, url
from .AddCarView import AddCarView
from .RideShareView import RideShareView
from .SignupView import SignupView
from views import rideshareindexView, signupView, executeSignup, addCar
from views import carView, deleteCar, executeDeleteCar, kickPassenger, executeKickPassenger
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('', 
	url(r'^$', rideshareindexView, name='ride_share.index'),
	url(r'^add_car/$', AddCarView.as_view(), name='add_car'),
	url(r'^(?P<carid>\d+)/signup/$', signupView, name='signup'),
	url(r'^(?P<carid>\d+)/executeSignup/$', executeSignup, name='executeSignup'),
	url(r'^(?P<carid>\d+)/$', carView, name='carDetails'),
	url(r'^(?P<carid>\d+)/deleteCar/$', deleteCar, name='deleteCar'),
	url(r'^(?P<carid>\d+)/executeDelete/$', executeDeleteCar, name='executeDeleteCar'),
	url(r'^(?P<carid>\d+)/kickPassenger/(?P<pk>\d+)/$', kickPassenger, name='kickPassenger'),
	url(r'^(?P<carid>\d+)/executeKick/(?P<pk>\d+)$', executeKickPassenger, name='executeKickPassenger'),
)
