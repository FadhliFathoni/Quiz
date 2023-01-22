from django.db import models
from manager.models import Soal

class UserSubmit(models.Model):
    user = models.CharField(max_length=20)
    soal = models.ForeignKey(Soal, on_delete=models.CASCADE)
    jawaban = models.TextField(null=True)
    status = models.CharField(max_length=20, default="Unsolved")

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}( {} )".format(self.user,self.soal, self.status)