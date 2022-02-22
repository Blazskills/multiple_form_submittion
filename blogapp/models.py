from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    body = models.TextField()


    def __str__(self):
        return "%s (%s)" % (self.name, self.email)