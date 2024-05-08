from django.db import models

# Create your models here.


class contactUs(models.Model):
    name =models.CharField(max_length=500)
    email = models.EmailField()
    phone =models.CharField(max_length=50)
    project=models.CharField(max_length=500)
    subject =models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name