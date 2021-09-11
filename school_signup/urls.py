from rest_framework import routers
from django.urls import path ,include
from .views import *



app_name = 'blog'


router = routers.SimpleRouter()
router.register('student-info', StudentInfoViewSet,basename='student-info')
router.register('family-info', FamilyInfoViewSet,basename='family-info')

urlpatterns = [
    path('',include(router.urls)),
]
