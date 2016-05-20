from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False, unique=True)

# Create your models here.
class Context(models.Model):
    attribute = models.CharField(max_length=255, blank=False, null=False)
    means = models.CharField(max_length=1000, blank=False, null=False, default="http://schema.org/Thing")
    type = models.CharField(max_length=1000, blank=True, null=True)
    classname = models.ForeignKey(Class, related_name="contexts")
