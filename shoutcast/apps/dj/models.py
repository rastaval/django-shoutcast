from django.db import models
from django.contrib.auth.models import User



class DjPerson(models.Model):
    user = models.ForeignKey(User)
    handle = models.CharField(max_length=420)
    bio = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.handle


class DjShow(models.Model):
    dj = models.ForeignKey(DjPerson)
    show_name = models.CharField(max_length=420)
    description = models.TextField()
    show_file = models.FileField(upload_to="shows/")
    date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return self.show_name


class CoolLinks(models.Model):
    url = models.CharField(max_length=420)
    name = models.CharField(max_length=420)

    def __unicode__(self):
        return self.url