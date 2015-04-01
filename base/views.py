#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.templatetags.static import static
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout, update_session_auth_hash
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.views.generic.edit import FormView

from os import listdir
from os.path import isfile, join


from helpers import getMenuInfo

def index(request):
	return render(request, 'index.html')

@login_required(login_url = '/loginRequired')
def home(request):
	# TODO
	return render(request, 'home.html', {'menu' : getMenuInfo(request), 'title' : "Home"})
		
def coverPic(request):
	files = '{"pics": ['
	path = 'base/static/cover_pics/'
	temp = listdir(path);
	for f in temp:
		if isfile(join(path, f)):
			filename = static('cover_pics/' + f)
			files += '"'+filename+'",'
	files = files[:-1]
	files += "]}"
	return HttpResponse(files)
