from base.helpers import isPreviousEvent, isUpcomingEvent

from tools.item_share.ItemShareView import ItemShareView
from tools.money_share.MoneyShareTool import MoneyShareTool
from tools.upload_pics.UploadPicsTool import UploadPicsView
from tools.weather.weatherTool import WeatherView
from tools.allergy_list.allergyListTool import AllergyListView
from tools.ride_share.RideshareView import RideshareView
from tools.schedule.ScheduleTool import ScheduleView

from tools.maps.MapView import MapView

from tools.forum.views import ForumView




class ToolManager:
	@staticmethod
	def getTools(event):
		eventType = event.eventType
		tools = []
		context = {}
		# Tools for Previous Events
		if isPreviousEvent(event):
			tools.append(MoneyShareTool)
			context['money_share'] = MoneyShareTool.getContext(event)
			tools.append(UploadPicsView)
			context['upload_pics'] = UploadPicsView.getContext(event)
		# Tools for Upcoming Events
		if isUpcomingEvent(event):
			tools.append(ItemShareView)
			context['item_share'] = ItemShareView.getContext(event)
			tools.append(ScheduleView)
			context['schedule'] = ScheduleView.getContext(event)
			tools.append(MoneyShareTool)
			context['money_share'] = MoneyShareTool.getContext(event)
			tools.append(AllergyListView)
			context['allergy_list'] = AllergyListView.getContext(event)
			tools.append(WeatherView)
			context['weather'] = WeatherView.getContext(event)
			tools.append(RideshareView)
			context['ride_share'] = RideshareView.getContext(event)

		# Tools for both Upcoming and Previous Events
		
		tools.append(ForumView)
		context['forum'] = ForumView.getContext(event)
		tools.append(MapView)
		context['maps'] = MapView.getContext(event)
		return {'tools' : tools, 'context' : context}
