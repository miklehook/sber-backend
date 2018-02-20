from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class Client(models.Model):
    """
    Log Model
    Defines the attributes of a log
    """

    FIO = models.CharField(u'FIO', blank=False, null=True, max_length=300)
