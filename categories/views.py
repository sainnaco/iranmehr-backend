from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from permissions.permissions import IsStaffOrReadOnly,IsAuthorOrReadOnly
from .models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['main_category','sub_category'] #or author__username #علاوه بر علامت مساوی علامت های دیگر هم هست
    search_fields = ['main_category','sub_category']
    # ordering_fields = ['']

    def get_permissions(self):

        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]
