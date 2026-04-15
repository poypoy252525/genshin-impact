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
    EQUIP_BRACER = 'equip_bracer', 'Flower of Life'
    EQUIP_NECKLACE = 'equip_necklace', 'Plume of Dusk'
    EQUIP_RING = 'equip_ring', 'Sands of Eon'
    EQUIP_SHOES = 'equip_shoes', 'Goblet of Eon'
    EQUIP_DRESS = 'equip_dress', 'Circlet of Logos'

class ArtifactSuit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ArtifactSuitType.choices)
    max_level = models.PositiveSmallIntegerField()
    
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
    affix_list = models.ForeignKey(ArtifactAffixList, on_delete=models.CASCADE, null=True, blank=True)
    rarities = models.ManyToManyField(Rarity, related_name='artifacts')
    icon = models.ImageField(upload_to='images/artifacts', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    suit = models.ForeignKey(ArtifactSuit, on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name