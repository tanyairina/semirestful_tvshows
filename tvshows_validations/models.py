from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title'])<3:
            errors['title'] = "Show Title should be at least 2 characters"
        if len(postData['network'])<3:
            errors['network'] = "Show Network should at least 3 characters"
        if len(postData['description']) != 0 and len(postData['description'])<10:
            errors['description'] = "Show Description should at least 10 characters"
        if datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = "Release Date should be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    
