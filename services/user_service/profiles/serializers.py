from rest_framework import serializers
from .models import UserProfile, UserDocument

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['created_at', 'updated_at']


class UserDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocument
        exclude = ['created_at', 'verified_at']
