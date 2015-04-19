from tools.ToolView import ToolView

class MoneyShareTool(ToolView):
	tile_template = "money_share/money_share_tile.html"

	@staticmethod
	def getIdentifier():
		return "money_share"
