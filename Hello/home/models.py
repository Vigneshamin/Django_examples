from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    user = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.IntegerField()
    comment = models.TextField()


class Contactus(models.Model):
    name = models.CharField(max_length=122)
    user = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.BigIntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name



