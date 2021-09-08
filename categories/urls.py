from rest_framework import routers
from django.urls import path ,include
from .views import *



app_name = 'categories'


router = routers.SimpleRouter()
router.register('Categories',CategoryViewSet,basename='Categories')
urlpatterns = [
    path('',include(router.urls)),
]
