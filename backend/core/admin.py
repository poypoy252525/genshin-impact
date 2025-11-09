from django.contrib import admin
from .models import Character, User, Weapon, Role


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'element', 'quality', 'model_type', 'weapon']


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['type']
