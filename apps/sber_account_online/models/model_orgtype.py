from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class OrgType(models.Model):
    """
    Log Model
    Defines the attributes of a log
    """

    short_name = models.CharField(u'ShortName', blank=False, null=False, max_length=10,)
    full_name = models.CharField(u'FullName', blank=False, null=False, max_length=300,)
