import uuid
from django.db import models

class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_icon = models.ImageField(upload_to='images/characters')

    def __str__(self):
        return self.name