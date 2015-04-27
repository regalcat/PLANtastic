from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView

from .models import MsPaymentModel

class EditPaymentView(UpdateView):
	model = MsPaymentModel
	template_name = "money_share/edit_payment_form.html"
	fields = ['amount']
	success_url = "../"

	def post(self, request, eventid, pk):
		if "delete" in request.POST:
			MsPaymentModel.objects.get(id=pk).delete()
			return HttpResponseRedirect(self.success_url)
		else:
			return super(EditPaymentView, self).post(eventid, pk) 
