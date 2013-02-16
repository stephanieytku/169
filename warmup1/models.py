from django.db import models

# Create your models here.

class userModel(models.Model):
    
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    count = models.IntegerField()


    def __unicode__(self):
        return self.name