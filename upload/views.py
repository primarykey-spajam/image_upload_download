from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route, list_route
import os
from rest_framework.response import Response

from .models import Image
from .serializer import ImageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

UPLOAD_DIR = 'media/images/'

class ImageSet(APIView):
    # https://qiita.com/egplnt/items/e5c14199ed901fe1fd66*
    # request must have PARAMS['id'] & FILES['file']
    serializer_class = ImageSerializer

    def create(self, request, format=None):
        file = request.FILES['file']
        path = os.path.join(UPLOAD_DIR, file.name)
        destination = open(path, 'wb')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

        if not os.path.exists(path):
            print('File not found:', path)
            return create_render(request)

        image, created = Image.objects.get_or_create(filepath=path)
        if created:
            image.save()

        return Response({'message': 'OK'})

class ImageGet(APIView):
    # http://flame-blaze.net/archives/4999
    # request must have PARAMS['id']
    def get(self, request, format=None):
        obj=Image.objects.filter(id=request.PARAMS['id'])
        serializers = ImageSerializer(obj, many=False)
        return Response(serializers.data, status.HTTP_200_OK)
