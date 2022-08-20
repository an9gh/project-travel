from django.db import models
import datetime


# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return (self.name)

class Destination(models.Model):
    newname = models.CharField(max_length=100)
    desc_2 = models.TextField()
    img_2 = models.ImageField(upload_to = 'pictures_2')
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return (self.newname)
    
    def datepublished(self):
        return self.pub_date.strftime('%B %d %Y')

    



