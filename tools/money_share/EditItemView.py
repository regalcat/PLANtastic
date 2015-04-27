from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView

from .models import MsItemModel

class EditItemView(UpdateView):
	model = MsItemModel
	template_name = "money_share/edit_item_form.html"
	fields = ['name', 'cost']
	success_url = "../"

	def post(self, request, eventid, pk):
		if "delete" in request.POST:
			MsItemModel.objects.get(id=pk).delete()
			return HttpResponseRedirect(self.success_url)
		else:
			return super(EditItemView, self).post(eventid, pk) 
