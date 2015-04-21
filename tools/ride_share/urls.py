from django.conf.urls import patterns, url
from .AddCarView import AddCarView
from .RideShareView import RideShareView
from .SignupView import SignupView
from views import rideshareindexView, signupView, addCar
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('', 
	url(r'^$', rideshareindexView, name='ride_share.index'),
	url(r'^add_car/$', AddCarView.as_view(), name='add_car'),
	url(r'^signup/$', SignupView.as_view(), name='signup'),
)
