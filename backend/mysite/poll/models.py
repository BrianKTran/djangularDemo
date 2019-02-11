
from django.db import models

# Create your models here.
class ExampleModel(models.Model):
	firstname    = models.CharField(max_length=200)
	lastname     = models.CharField(max_length=200)

class AvocadoModel(models.Model):
	avocadoType  = models.CharField(max_length=200)
	avocadoPrice = models.CharField(max_length=200)
# from poll.models import AvocadoModel
# p = AvocadoModel(avocadoType='Peter', avocadoPrice='Paul')
# p.save()


# from poll.models import AvocadoModel
# p = AvocadoModel(avocadoType='hass', avocadoPrice='.98')
# p.save()
