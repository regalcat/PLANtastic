from django.http import HttpResponse
from django.template import RequestContext, loader
from base.forms import InviteForm
from django.views.generic.edit import FormView


def test(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

#The class that handles inviting people via email and then displays an html page
class InviteView(forms.Form):
	temp_name = ''
	form_class = InviteForm
	success_url = '/thanks/'
	
	def valid_email(self, form):
		
		form.send_invite()
		return super(InviteView, self).valid_email(form)
