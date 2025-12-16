from django.db import models

# Create your models here.
class Todos(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=25)
    content = models.TextField()
    is_done = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'todos'
