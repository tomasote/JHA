from django.db import models
from django.conf import settings

class Entry(models.Model):
    serviceId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description