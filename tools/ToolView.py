from django.http import HttpResponse
from django.views.generic import View

class ToolView(View):
	@staticmethod
	def getTileTemplate():
	    return ("tools/default.html", ())

	@staticmethod
	def Identifier():
		return "tools"

	@staticmethod
	def getContext(event):
		return {}

