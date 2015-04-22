from tools.ToolView import ToolView
from tools.schedule.models import ScheduleModel
import datetime
from django.utils import timezone
from events.models import EventModel



class ScheduleView(ToolView):
	tile_template = "schedule/scheduleTile.html"

	@staticmethod
	def getIdentifier():
		return "schedule"
	
	@staticmethod
	def getContext(event_):

		activities = ScheduleModel.objects.filter(event = event_).order_by("start_date")	
		today = timezone.now()
		context = {}
		
		for i in range(len(activities)):
			if today < activities[i].start_date:
				context['name'] = activities[i].name
				context['start_date'] = activities[i].start_date
				context['end_date'] = activities[i].end_date
				context['description'] = activities[i].description
				break

		return context
