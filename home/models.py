from django.db import models

# Create your models here.
class contact(models.Model):
    Name=  models.CharField(max_length=122, null=True)
    Email =  models.CharField(max_length=122, null=True)
    phone =  models.CharField(max_length=122, null=True)
    desc  =  models.TextField(null=True)
    date =   models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.Name