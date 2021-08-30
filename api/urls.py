from django.urls import path
from .views import *


app_name = 'api'


urlpatterns = [
    path('',ArticleViewSet,name='articles'),
    path('users/',UserViewSet,name='user'),
    # path('users/<int:pk>',UserDetail.as_view(),name='list'),
    # path('<slug:slug>',ArticleDetail.as_view(),name='list'),
]