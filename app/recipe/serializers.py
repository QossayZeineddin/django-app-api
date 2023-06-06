"""
Serializers for recipe APIs View
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

    # def create(self, validated_data):
    #     """Create a new recipe."""
    #     return Recipe.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """Update recipe."""


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        model = RecipeSerializer.Meta.model
        fields = RecipeSerializer.Meta.fields + ['description']
