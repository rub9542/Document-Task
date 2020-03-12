from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=User
        fields=('name','phone',)

class DocumentSerializer(serializers.ModelSerializer):
    owner=UserSerializer
    class Meta:
        model=Document
        fields=('owner','created_time','type','source_type','source_id',)