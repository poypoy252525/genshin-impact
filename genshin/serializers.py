from rest_framework import serializers
from .models import Character, Artifact, Rarity, ArtifactSuit, ArtifactAffixList

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'image_icon']
        read_only_fields = ['id']
        
        
class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = ['level']
        
        
class ArtifactSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactSuit
        fields = ['id', 'name', 'type', 'icon', 'max_level', 'description']
        read_only_fields = ['id']


class ArtifactSerializer(serializers.ModelSerializer):
    rarities = RaritySerializer(many=True)
    
    class Meta:
        model = Artifact
        fields = ['id', 'name', 'rarities', 'icon']
        read_only_fields = ['id']
        

class ArtifactAffixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactAffixList
        fields = ['name']
 

class ArtifactDetailSerializer(serializers.ModelSerializer):
    suit = ArtifactSuitSerializer(many=True)
    affix_list = ArtifactAffixListSerializer(many=True)
    rarities = RaritySerializer(many=True)
    
    class Meta:
        model = Artifact
        fields = ['id', 'name', 'rarities', 'icon', 'suit', 'affix_list']
        read_only_fields = ['id']