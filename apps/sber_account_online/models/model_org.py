from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class Organization(models.Model):
    """
    Log Model
    Defines the attributes of a log
    """

    INN = models.PositiveSmallIntegerField(u'INN', blank=False, null=True)
    OGRN = models.PositiveSmallIntegerField(u'OGRN', blank=False, null=True)