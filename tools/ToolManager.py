from base.helpers import isPreviousEvent, isUpcomingEvent

from tools.item_share.ItemShareView import ItemShareView
from tools.upload_pics.UploadPicsTool import UploadPicsView

class ToolManager:
	@staticmethod
	def getTools(event):
		eventType = event.eventType
		tools = []
		if isPreviousEvent(event):
			tools.append(UploadPicsView)
		if isUpcomingEvent(event):
			tools.append(ItemShareView)
		return tools
