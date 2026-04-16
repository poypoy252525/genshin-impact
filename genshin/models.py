import uuid
from django.db import models

class RarityLevel(models.TextChoices):
    ONE_STAR = '1', '1 Star'
    TWO_STAR = '2', '2 Star'
    THREE_STAR = '3', '3 Star'
    FOUR_STAR = '4', '4 Star'
    FIVE_STAR = '5', '5 Star'

class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_icon = models.ImageField(upload_to='images/characters')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ArtifactAffixList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class ArtifactSuitType(models.TextChoices):
    EQUIP_BRACER = 'EQUIP_BRACER', 'Flower of Life'
    EQUIP_NECKLACE = 'EQUIP_NECKLACE', 'Plume of Dusk'
    EQUIP_RING = 'EQUIP_RING', 'Sands of Eon'
    EQUIP_SHOES = 'EQUIP_SHOES', 'Goblet of Eon'
    EQUIP_DRESS = 'EQUIP_DRESS', 'Circlet of Logos'

class ArtifactSuit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ArtifactSuitType.choices, blank=True, null=True)
    max_level = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Rarity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.CharField(max_length=1, choices=RarityLevel.choices)
    
    class Meta:
        verbose_name_plural = 'Rarities'
    
    def __str__(self):
        return self.level
    
class Artifact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    affix_list = models.ManyToManyField(ArtifactAffixList, related_name='artifacts', blank=True)
    rarities = models.ManyToManyField(Rarity, related_name='artifacts')
    icon = models.ImageField(upload_to='images/artifacts', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    suit = models.ManyToManyField(ArtifactSuit, related_name='artifacts', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name