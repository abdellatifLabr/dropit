from django.db import models
from datetime import timedelta
from django.utils import timezone

class File(models.Model):
    _hash = models.TextField(unique=True, max_length=32, editable=False)
    _file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created + timedelta(days=1)
    