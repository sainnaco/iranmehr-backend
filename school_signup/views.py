
# اینارو کامنت کردم چون میخام خودم ویوست بنویسم
# from rest_framework.generics import RetrieveAPIView  #ListAPIView , RetrieveUpdateDestroyAPIView ,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.models import *
from .serializers import *
from permissions.permissions import IsStaffOrReadOnly,IsAuthorOrReadOnly
from rest_framework import filters #خصوصی بدیم ولی گلوبال دادیم

class StudentInfoViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = ['birth_day','birth_month','birth_year','register_time','grade','darsad']

    def get_permissions(self):

        if self.action in ['create','update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class FamilyInfoViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilyInfoSerializer
    filterset_fields = '__all__'
    search_fields = '__all__'
    # ordering_fields = []

    def get_permissions(self):

        if self.action in ['create','update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


