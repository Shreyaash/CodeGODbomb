from django.db import models

class Attackinfo(models.Model):

    mobile_n = models.CharField(max_length=100)
    frequency_n = models.CharField(max_length=100)


    def __str__(self):
        return self.mobile_n + "-" + self.frequency_n
