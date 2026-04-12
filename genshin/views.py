from rest_framework.viewsets import ModelViewSet
from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer