from rest_framework import serializers
from . import models
from qupang.images import serializers as images_serializers

class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.CountImageSerializer(many=True, read_only=True)
    # For the "serializers.ReadOnlyField()"
    # I don't want UserProfileSerializer to think that I can modify this fields
    # This is just, a property of my model
    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images',
        )

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )