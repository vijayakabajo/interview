from django.db import models

# Create your models here.
class Todos(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=64, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'todos'
