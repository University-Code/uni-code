# reference
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

''' 
A profile relation that extends the built in User Model

    NOTE: You can query both Users & their respective Profiles together like so:

    users = User.objects.all().select_related('profile')

''' 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    graduation_year = models.IntegerField()

