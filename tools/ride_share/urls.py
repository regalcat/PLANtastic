from django.conf.urls import patterns, url

from .RideShareView import RideShareView

from views import rideshareindexView, signupView, executeSignup, addCar, leaveCar, executeLeaveCar
from views import carView, deleteCar, executeDeleteCar, kickPassenger, executeKickPassenger


urlpatterns = patterns('', 
	url(r'^$', rideshareindexView, name='ride_share.index'),
	url(r'^add_car/$', addCar, name='add_car'),
	url(r'^(?P<carid>\d+)/signup/$', signupView, name='signup'),
	url(r'^(?P<carid>\d+)/executeSignup/$', executeSignup, name='executeSignup'),
	url(r'^(?P<carid>\d+)/$', carView, name='carDetails'),
	url(r'^(?P<carid>\d+)/deleteCar/$', deleteCar, name='deleteCar'),
	url(r'^(?P<carid>\d+)/executeDelete/$', executeDeleteCar, name='executeDeleteCar'),
	url(r'^(?P<carid>\d+)/kickPassenger/$', kickPassenger, name='kickPassenger'),
	url(r'^(?P<carid>\d+)/executeKick/$', executeKickPassenger, name='executeKick'),
	url(r'^(?P<carid>\d+)/leaveCar/$', leaveCar, name='leaveCar'),
	url(r'^(?P<carid>\d+)/executeLeave/$', executeLeaveCar, name='executeLeave'),
)
