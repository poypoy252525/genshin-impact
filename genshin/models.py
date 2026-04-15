import uuid
from django.db import models

class Rarity(models.TextChoices):
    ONE_STAR = '1', '1 Star'
    TWO_STAR = '2', '2 Star'
    THREE_STAR = '3', '3 Star'
    FOUR_STAR = '4', '4 Star'
    FIVE_STAR = '5', '5 Star'

class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_icon = models.ImageField(upload_to='images/characters')

    def __str__(self):
        return self.name
    
    
class Artifact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rarity = models.CharField(max_length=1, choices=Rarity.choices)
    image_icon = models.ImageField(upload_to='images/artifacts')
    description = models.TextField()

    def __str__(self):
        return self.name