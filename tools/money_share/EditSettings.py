from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView

from .models import MsSettingsModel

class EditSettingsView(UpdateView):
	model = MsSettingsModel
	template_name = "money_share/edit_settings.html"
	fields = ['method']
	success_url = "../"
