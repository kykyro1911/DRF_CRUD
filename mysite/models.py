from django.db import models

# Create your models here.
class CRUD(models.Model):
    name = models.TextField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now=True)
