from rest_framework import routers
from django.urls import path ,include
from .views import *

app_name = 'categories'

router = routers.SimpleRouter()
router.register('categories',CategoryViewSet,basename='categories')
urlpatterns = [
    path('',include(router.urls)),
]
