from django.db import models

# models here

# card
class Card(models.Model):
    q = models.CharField(max_length=200)
    a = models.CharField(max_length=150)
    b = models.CharField(max_length=150)
    
    def __str__(self):
        return self.q
