from rest_framework import serializers
from . import models


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = '__all__'


class SignsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Signs
        fields = '__all__'
