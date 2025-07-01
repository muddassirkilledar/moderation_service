from rest_framework import serializers
from .models import Comment, User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Uses User.__str__, which returns the email

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'flagged', 'flag_reason', 'created_at']
        read_only_fields = ['user', 'flagged', 'flag_reason', 'created_at']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user