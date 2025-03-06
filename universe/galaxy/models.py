from django.db import models

class galaxy(models.Model):
    fristname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
