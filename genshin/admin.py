from django.contrib import admin
from .models import Character, Rarity, ArtifactAffixList, ArtifactSuit, Artifact

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ('level',)

@admin.register(ArtifactAffixList)
class ArtifactAffixListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ArtifactSuit)
class ArtifactSuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'max_level')
    list_filter = ('type',)
    search_fields = ('name',)

@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('name', 'source_id', 'suit', 'created_at')
    list_filter = ('rarities', 'suit')
    search_fields = ('name', 'description')
    filter_horizontal = ('rarities',)
