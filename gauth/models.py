from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class GAuth(models.Model):
    user = models.OneToOneField(User, related_name="gauth")
    token = models.CharField(max_length=100)

    def __unicode__(self):
        return "{} - {}".format(self.user.username, self.token)
