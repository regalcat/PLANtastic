from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import UploadedPicModel
from base.permissions import memberCheck

class EditPicView(UpdateView):
	model = UploadedPicModel
	template_name = "upload_pics/edit_pic_form.html"
	fields = ['title', 'caption']
	success_url = "../"

	
