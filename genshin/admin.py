from django.contrib import admin
from .models import Character, Rarity, ArtifactAffixList, ArtifactSuit, Artifact, Material, MaterialSource

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

class MaterialSourceInline(admin.TabularInline):
    model = MaterialSource
    extra = 0

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'external_id')
    search_fields = ('name',)
    inlines = [MaterialSourceInline]
    filter_horizontal = ('rarities',)

@admin.register(MaterialSource)
class MaterialSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'material')
    search_fields = ('name',)
