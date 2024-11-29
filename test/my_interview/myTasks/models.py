from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pk} {self.title} {self.description} {self.status}"
    
