from rest_framework import serializers
from .models import Category, Lectures


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectures
        fields = '__all__'
