from rest_framework import serializers
from .models import Project, ProjectUpdate, ProjectFile


class ProjectUpdateSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True)

    class Meta:
        model = ProjectUpdate
        fields = ['id', 'message', 'author', 'author_name', 'created_at']
        read_only_fields = ['author']

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['id', 'file', 'uploaded_by', 'uploaded_at']
        read_only_fields = ['uploaded_by']

class ProjectSerializer(serializers.ModelSerializer):
    updates = ProjectUpdateSerializer(many=True, read_only=True)
    files = ProjectFileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['created_by']
