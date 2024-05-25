from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


class CategoryListAPIView(APIView):
    def get(self, request):
        category = models.Categories.objects.all()
        serializer = serializers.CategorySerializers(category, many=True)
        serializer_data = {
            'category': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class SignsListAPIView(APIView):
    def get(self, request):
        signs = models.Signs.objects.all()
        serializer = serializers.SignsSerializers(signs, many=True)
        serializer_data = {
            'sign': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)