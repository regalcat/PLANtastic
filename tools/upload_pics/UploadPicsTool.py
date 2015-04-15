from tools.ToolView import ToolView

from .MainView import MainView as UploadPicView
from .models import UploadedPicModel

class UploadPicsView(ToolView):
	tile_template = "upload_pics/upload_pics_tile.html"

	@staticmethod
	def getIdentifier():
		return "upload_pics"
	
	@staticmethod
	def getContext(event_):
		context = {}
		context['pics'] = UploadedPicModel.objects.filter(event_id = event_.eventid)
		return context
