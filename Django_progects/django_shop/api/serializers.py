from rest_framework import serializers

from main.models import Ads, Comment


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id', 'title', 'content', 'price', 'created')


class AdsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id', 'title', 'content', 'price', 'created', 'contacts', 'image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('ads', 'author', 'content', 'created')
