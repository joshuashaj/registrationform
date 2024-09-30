from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "details"