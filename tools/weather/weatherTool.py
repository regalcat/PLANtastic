from tools.ToolView import ToolView
from tools.weather.models import WeatherModel
from base.permissions import memberCheck, isCreator, isCoplanner

class WeatherView(ToolView):
	tile_template = "weather/weatherTile.html"

	@staticmethod
	def getIdentifier():
		return "weather"
	
	@staticmethod
	def getContext(event_):
		context = {}
		information = WeatherModel.objects.filter(event = event_)
		
		if information.count() == 1:
			context['state'] = information[0].get_state_display
			context['degreeType'] = information[0].degreeType

			city = information[0].city.title()
			new = ""
			for i in range(len(city)):
				if city[i] == " ":
					new = new + "+"
				else:
					new = new + city[i]
			context['city'] = new

		return context
	
