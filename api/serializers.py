from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Recipe, UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        depth = 1


class UserInfoSerializer(serializers.ModelSerializer):
    recipe_created = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'
        read_only_fields = ('friends', 'recipe_collection')
        depth = 1
