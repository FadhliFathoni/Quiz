from django.db import models
from manager.models import Soal

class UserSubmit(models.Model):
    user = models.CharField(max_length=20)
    soal = models.ForeignKey(Soal, on_delete=models.CASCADE)