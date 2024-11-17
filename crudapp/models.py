from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    salary = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    cname = models.TextField()

    class Meta:
        db_table = 'users'  
        managed = False  

    def __str__(self):
        return self.name



