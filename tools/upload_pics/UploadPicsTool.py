from tools.ToolView import ToolView

class UploadPicsView(ToolView):
	tile_template = "upload_pics/upload_pics_tile.html"

	def getMainPageUrl():
		return "upload_pics"
