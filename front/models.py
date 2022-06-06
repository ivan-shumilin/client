from django.db import models

# Create your models here.
class Forecast(models.Model):
    sing = models.CharField(max_length=200, null=True)


    def __str__(self):
        return f'{self.sing}'