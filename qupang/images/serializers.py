from rest_framework import serializers
from . import models
from qupang.users import models as user_model
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class SmallImageSerializer(serializers.ModelSerializer):

    """ Used For the Notifications """
    class Meta:
        model = models.Image
        fields = ('file',)

class CountImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )
    

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_model.User
        fields = (
            'username',
            'profile_image',
        )


class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'creator',
            'comments',
            'like_count',
            'created_at',
            'tags',
        )


class InputImageSerializer(serializers.ModelSerializer):

    # fields in fields are all required field to update DATABASE
    # to avoid this >> file = serializers.FileField(required=False)
    # OR to use "partial=True" << IMPORTANT
    class Meta:
        model = models.Image
        fields = (
            'file','location','caption',
        )

