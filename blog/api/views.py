
# اینارو کامنت کردم چون میخام خودم ویوست بنویسم
# from rest_framework.generics import RetrieveAPIView  #ListAPIView , RetrieveUpdateDestroyAPIView ,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
from blog.models import *
from .serializers import *
from permissions.permissions import IsStaffOrReadOnly,IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import filters #خصوصی بدیم ولی گلوبال دادیم

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['stutus','author'] #or author__username #علاوه بر علامت مساوی علامت های دیگر هم هست
    search_fields = ['title','author','content']
    ordering_fields = ['publish','stutus']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


