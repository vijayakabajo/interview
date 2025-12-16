from django.db import models

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'users'