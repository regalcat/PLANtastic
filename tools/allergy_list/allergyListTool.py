from tools.ToolView import ToolView
from tools.allergy_list.models import AllergyModel
from tools.allergy_list.models import *


class AllergyListView(ToolView):
	tile_template = "allergy_list/allergyTile.html"

	@staticmethod
	def getIdentifier():
		return "allergy_list"
	
	@staticmethod
	def getContext(event_):
		eventid = event_.eventid
		
		vegetarian = getCountVegetarian(eventid)
		vegan = getCountVegan(eventid)
		lactose = getCountLactose(eventid)
		gluten = getCountGluten(eventid)
		nuts = getCountNuts(eventid)

		context = {'vegetarian' : vegetarian, 'vegan' : vegan, 'lactose' : lactose, 'gluten' : gluten, 'nuts' : nuts}

		return context
