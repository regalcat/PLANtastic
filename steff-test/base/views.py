from base.forms import InviteForm
from django.views.generic.edit import FormView

class InviteView(FormView):
	template_name = 'invite.html'
	form_class = InviteForm
	success_url = '/invite-sent/'
	
	#Called when a valid form is submitted
	def form_valid(self, form):
		form.send_email()
		return super(InviteView, self).form_valid(form)

