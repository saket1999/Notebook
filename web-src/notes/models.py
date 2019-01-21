from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.contrib.postgres.fields import JSONField


User = get_user_model()


class NoteBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=50)
    description = models.TextField(null=True, max_length=360)
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())
    data = JSONField()

    class Meta:
        db_table = 'notebooks'
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'

