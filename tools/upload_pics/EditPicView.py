from django.views.generic.edit import UpdateView

from .models import UploadedPicModel

class EditPicView(UpdateView):
	model = UploadedPicModel
	template_name = "upload_pics/edit_pic_form.html"
	fields = ['title', 'caption']
	success_url = "../"

