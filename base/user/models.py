from django.db import models

class UserModel(models.Model):
        userID = models.IntegerField(primary_Key = True)
        realName = models.CharField(max_length = 20)
        email = models.EmailField()
        password = models.CharField(max_length = 50)
        birthday = models.DateField()


        def __unicode__(self):
                return self.realName

        def getPassword(self):
                return self.password





