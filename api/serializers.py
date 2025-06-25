from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'flagged', 'flag_reason', 'created_at']
        read_only_fields = ['flagged', 'flag_reason', 'created_at']