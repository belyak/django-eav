import six
from django.db import models


@six.python_2_unicode_compatible
class Patient(models.Model):
    class Meta:
        app_label = 'eav'

    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


@six.python_2_unicode_compatible
class Encounter(models.Model):
    class Meta:
        app_label = 'eav'

    num = models.PositiveSmallIntegerField()
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return '%s: encounter num %d' % (self.patient, self.num)

