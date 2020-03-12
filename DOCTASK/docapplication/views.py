from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET','POST'])
def api_document_list_view(request):
    document=Document.objects.all()
    if request.method=='GET':
        serializer=DocumentSerializer(document,many=True)
        return Response(serializer.data)
    if request.method=='Post':
        serializer=DocumentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)