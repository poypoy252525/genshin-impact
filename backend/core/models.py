from email.policy import default
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)


class Element(models.TextChoices):
    PYRO = "pyro", "Pyro"
    HYDRO = "hydro", "Hydro"
    ELECTRO = "electro", "Electro"
    CRYO = "cryo", "Cryo"
    ANEMO = "anemo", "Anemo"
    GEO = "geo", "Geo"
    DENDRO = "dendro", "Dendro"


class RoleType(models.TextChoices):
    DPS = "dps", "DPS"
    SUB_DPS = "sub-dps", "Sub-DPS"
    SUPPORT = "support", "Support"
    HEALER = "healer", "Healer"
    BUFFER = "buffer", "Buffer"


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type = models.CharField(max_length=20, choices=RoleType.choices, unique=True)

    def __str__(self) -> str:
        return self.get_type_display()


class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    element = models.CharField(max_length=10, choices=Element.choices)
    model_type = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role, related_name="characters", blank=True)
