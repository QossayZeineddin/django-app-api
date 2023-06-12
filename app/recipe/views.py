"""
Views for recipe model api
"""

from rest_framework import viewsets
from rest_framework import authentication, permissions

from core.models import Recipe
from . import serializers
from user.authentication import ExpiringTokenAuthentication


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """override  method used to create a new recipe """
        serializer.save(user=self.request.user)
