from django.http import HttpResponse
from django.views.generic import View

class ToolView(View):
	def getTileTemplate():
	    return ("tools/default.html", ())

	def getMainPageUrl():
		return "default"

