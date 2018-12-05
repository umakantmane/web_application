from django.db import models

class Collage(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique= True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)

    class Meta:

        db_table = 'collage'

