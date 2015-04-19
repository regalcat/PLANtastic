from django.views.generic.edit import UpdateView

from .models import MsItemModel

class EditItemView(UpdateView):
	model = MsItemModel
	template_name = "money_share/edit_item_form.html"
	fields = ['name', 'cost']
	success_url = "../"

