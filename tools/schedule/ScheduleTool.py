from tools.ToolView import ToolView
from tools.schedule.models import ScheduleModel



class ScheduleView(ToolView):
	tile_template = "schedule/scheduleTile.html"

	@staticmethod
	def getIdentifier():
		return "schedule"
	
	@staticmethod
	def getContext(event_):
		context = {}

		return context
