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
    list_display = ('name', 'external_id', 'display_suit', 'created_at')
    list_filter = ('rarities',)
    search_fields = ('name', 'description')
    filter_horizontal = ('rarities',)

    def display_suit(self, obj):
        return ", ".join([s.name for s in obj.suit.all()])
    display_suit.short_description = 'Suit'
