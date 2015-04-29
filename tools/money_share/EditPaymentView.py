from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import MsPaymentModel
from base.permissions import memberCheck
from events.models import EventModel

class EditPaymentView(UpdateView):
	model = MsPaymentModel
	template_name = "money_share/edit_payment_form.html"
	fields = ['amount']
	success_url = "../"

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid, pk):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		if "delete" in request.POST:
			MsPaymentModel.objects.get(id=pk).delete()
			return HttpResponseRedirect(self.success_url)
		else:
			return super(EditPaymentView, self).post(eventid, pk) 
