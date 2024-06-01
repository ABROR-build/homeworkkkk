# rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.decorators import api_view

# local modules
from . import serializers
from . import models


class CreateApiView(ListCreateAPIView):
    queryset = models.Signs.objects.all()
    serializer_class = serializers.SignsSerializers


@api_view(['GET'])
def get(self):
    signs = models.Signs.objects.all()
    serializer = serializers.SignsSerializers(signs, many=True)
    serializer_data = {
        'sign': serializer.data,
        'status': 'success',
        'status_code': status.HTTP_200_OK
    }
    return Response(serializer_data)
