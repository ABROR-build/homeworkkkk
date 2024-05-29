# rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

# local modules
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


class SignsDetailView(APIView):
    def get(self, request, pk):
        try:
            signs = models.Signs.objects.get(pk=pk)
            serializer = serializers.SignsSerializers(signs)
            serializer_data = {
                'sign': serializer.data,
                'status': 'success',
                'status_code': status.HTTP_200_OK
            }
        except Exception as exp:
            serializer_data = {
                'Error': str(exp) + f" Moron item with id-{pk} is not there",
                'status': 'ERROR',
                'status code': status.HTTP_404_NOT_FOUND,
            }
        finally:
            return Response(serializer_data)


class SignsDeleteView(APIView):
    def delete(self, request, pk):
        try:
            signs = models.Signs.objects.get(pk=pk)
            signs.delete()
            serializer_data = {
                'sign': f'item with id-{pk} is deleted',
                'status': 'success',
                'status_code': status.HTTP_200_OK
            }
        except Exception as exp:
            serializer_data = {
                'Error': str(exp) + f" Moron you can't delete item with id-{pk} because it is not there",
                'status': 'ERROR',
                'status code': status.HTTP_404_NOT_FOUND,
            }
        finally:
            return Response(serializer_data)
