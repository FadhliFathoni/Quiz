from django.db import models

# Create your models here.
class Soal(models.Model):
    
    category = (
        ("Easy","Easy"),
        ("Medium","Medium"),
        ("Hard","Hard"),
    )

    data = (
        ("Java","Java"),
        ("HTML","HTML"),
        ("Kotlin","Kotlin"),
        ("PHP","PHP"),
        ("Android","Android"),
        )

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50, null=True)
    code = models.TextField(null=True)
    category = models.CharField(max_length=20,choices=category)
    course = models.CharField(max_length=20,choices=data)
    contoh = models.ImageField(upload_to='static/img/', null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.course, self.title)