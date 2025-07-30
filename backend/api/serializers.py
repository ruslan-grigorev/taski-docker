"""Serializers for API models."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Represents a model used in the API."""

    class Meta:
        """Meta options for the TaskModel."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
