from django.db import models
from django.contrib.auth.models import User

def getUploadFileName(instance, filename):
	return "avatar_pics/%s" % (filename)

class Profile(models.Model):

	user = models.OneToOneField(User)
	birthday = models.DateField(blank=True, null=True)
	description = models.CharField(max_length = 500, blank = True, null = True)
	gender = models.CharField(max_length=10, blank=True, null=True, choices = (('Female','Female'), ('Male', 'Male'),))
	avatar = models.ImageField(upload_to = getUploadFileName, default='avatar_pics/default-profile.png', blank = True, null = True)

	def getBirthday(self):
		return self.birthday

	def getGender(self):
		return self.gender




User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
