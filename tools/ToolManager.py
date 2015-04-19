from base.helpers import isPreviousEvent, isUpcomingEvent

from tools.item_share.ItemShareView import ItemShareView
from tools.money_share.MoneyShareTool import MoneyShareTool
from tools.upload_pics.UploadPicsTool import UploadPicsView


class ToolManager:
	@staticmethod
	def getTools(event):
		eventType = event.eventType
		tools = []
		context = {}
		# Tools for Previous Events
		if isPreviousEvent(event):
			tools.append(UploadPicsView)
			context['upload_pics'] = UploadPicsView.getContext(event)
		# Tools for Upcoming Events
		if isUpcomingEvent(event):
			tools.append(ItemShareView)
			context['item_share'] = ItemShareView.getContext(event)
		# Tools for both Upcoming and Previous Events
		tools.append(MoneyShareTool)
		context['money_share'] = MoneyShareTool.getContext(event)
		return {'tools' : tools, 'context' : context}
