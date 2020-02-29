from django.db import models

class Location(models.Model):
    location = models.CharField(max_length =30)
    

    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ['location']
        
    def save_location(self):
        self.save()