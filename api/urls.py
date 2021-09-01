from rest_framework import routers
from django.urls import path , include
from .views import *


app_name = 'api'

router = routers.SimpleRouter()
router.register('users', UserViewSet,basename='users')
router.register('articles', ArticleViewSet,basename='articles')

urlpatterns = [
    path('',include(router.urls)),
    path('categories/',CategoryView.as_view(),name='categories'),
]