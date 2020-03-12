from rest_framework import routers
from . import views
from django.urls import path,include, re_path
from .views import *


urlpatterns =[
    path('doc/',api_document_list_view,name='document-objects'),
]