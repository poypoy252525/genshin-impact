from genshin.serializers import MaterialDetailSerializer
from genshin.serializers import MaterialSerializer
from genshin.models import Material
from rest_framework.viewsets import ModelViewSet
from .models import Character, Artifact
from .serializers import CharacterSerializer, ArtifactSerializer, ArtifactDetailSerializer

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class ArtifactViewSet(ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArtifactSerializer
        return ArtifactDetailSerializer
    
    
class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return MaterialSerializer
        return MaterialDetailSerializer