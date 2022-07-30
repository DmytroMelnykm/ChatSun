from django.db import models


# Create your models here.

class InfoHuman(models.Model):
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Born = models.DateTimeField()
    Age = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.Name, self.Surname)

