from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=254, blank=False)
    details = models.TextField(blank=False)
    
    def __str__(self):
        return self.email