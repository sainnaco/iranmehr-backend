from rest_framework import routers
from django.urls import path ,include
from .blog_api_views import *



app_name = 'blog'


router = routers.SimpleRouter()
router.register('articles', ArticleViewSet,basename='articles')

urlpatterns = [
    path('',include(router.urls)),
    path('categories/',CategoryView.as_view(),name='categories'),
]

# urlpatterns = [
#     path('',ArticleViewSet,name='articles'),
#     path('users/',UserViewSet,name='user'),
#     # path('users/<int:pk>',UserDetail.as_view(),name='list'),
#     # path('<slug:slug>',ArticleDetail.as_view(),name='list'),
# ]