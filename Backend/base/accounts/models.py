from django.db import models

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'users'
