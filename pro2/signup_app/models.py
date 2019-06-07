from django.db import models

# Create your models here.
class Signup_model(models.Model):
    name =models.CharField(max_length =264)
    email=models.EmailField()
    password =models.CharField(max_length =264)

    def __str__(self):
        return self.name
