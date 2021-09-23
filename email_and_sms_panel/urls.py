from rest_framework import routers
from django.urls import path ,include
from .views import *



app_name = 'email and sms panel'


router = routers.SimpleRouter()
router.register('email', EmailViewSet,basename='email')

urlpatterns = [
    path('',include(router.urls)),
    path('send-email/',send_email_task)
]

# urlpatterns = [
#     path('',ArticleViewSet,name='articles'),
#     path('users/',UserViewSet,name='user'),
#     # path('users/<int:pk>',UserDetail.as_view(),name='list'),
#     # path('<slug:slug>',ArticleDetail.as_view(),name='list'),
# ]