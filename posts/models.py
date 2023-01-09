from django.db import models
from django.conf import settings

# Create your models here.
class Cathegory(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    created = models.DateTimeField()
    changed = models.DateTimeField()
    cathegory = models.ForeignKey(
        'Cathegory',
        on_delete=models.CASCADE,
    )
    is_published =  models.BooleanField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )