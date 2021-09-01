from rest_framework.viewsets import ModelViewSet
from blog.models import *
from .serializers import *
from .permission import *
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView
#from rest_framework import filters #خصوصی بدیم ولی گلوبال دادیم

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status','author'] #or author__username
    search_fields = ['title','author','description']
    ordering_fields = ['publish','status']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,) 

    # filterset_fields = ['status','author'] #or author__username
    search_fields = ['name','email']
    ordering_fields = ['is_active','is_staff','is_active','is_admin']
    
class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsStaffOrReadOnly,) #فقط سوپریوزر قادر به تعین کنگوری باشد
