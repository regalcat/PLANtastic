from base.helpers import isPreviousEvent, isUpcomingEvent

from tools.item_share.ItemShareView import ItemShareView
from tools.upload_pics.UploadPicsTool import UploadPicsView
from tools.weather.weatherTool import WeatherView

class ToolManager:
	@staticmethod
	def getTools(event):
		eventType = event.eventType
		tools = []
		context = {}
		if isPreviousEvent(event):
			tools.append(UploadPicsView)
			context['upload_pics'] = UploadPicsView.getContext(event)
		if isUpcomingEvent(event):
			tools.append(ItemShareView)
			context['item_share'] = ItemShareView.getContext(event)
			tools.append(WeatherView)
			context['weather'] = WeatherView.getContext(event)
		return {'tools' : tools, 'context' : context}
