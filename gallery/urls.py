from rest_framework import routers
from django.urls import path ,include
from .views import *

app_name = 'gallery'

router = routers.SimpleRouter()
router.register('picture',PictureViewSet,basename='picture')
router.register('video',VideoViewSet,basename='video')

urlpatterns = [
    path('',include(router.urls)),
]
