from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField()




User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
