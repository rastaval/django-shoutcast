from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class DjPerson(models.Model):
    user = models.ForeignKey(User)
    handle = models.CharField(max_length=420)
    bio = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.handle


class DjShow(models.Model):
    dj = models.OneToOneField(User)
    show_name = models.CharField(max_length=420, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.show_name


class ShowArchive(models.Model):
    djshow = models.ForeignKey(DjShow)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    show_file = models.FileField(upload_to="/", blank=True, null=True)

    def __unicode__(self):
        return self.djshow


class CoolLinks(models.Model):
    url = models.CharField(max_length=420)
    name = models.CharField(max_length=420)

    def __unicode__(self):
        return self.url


@receiver(post_save, sender=User)
def create_show(sender, instance, created, **kwargs):
    if created:
        show, new = DjShow.objects.get_or_create(dj=instance, show_name="Change me please!", description="oh no i havent been channnnged")


