from django.urls import path, include
from rest_framework import routers
from .views import CharacterViewSet, ArtifactViewSet

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'artifacts', ArtifactViewSet, basename='artifact')

urlpatterns = [
    path('', include(router.urls)),
]
