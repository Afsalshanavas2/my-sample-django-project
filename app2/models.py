from django.db import models

class Teachers(models.Model):
    tname = models.CharField(max_length=50)
    tsubject = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tname}-{self.tsubject}"

# Create your models here.
