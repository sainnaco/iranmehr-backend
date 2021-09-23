from rest_framework.viewsets import ModelViewSet
from .serializers import VideoSerializer , PictureSerializer
from permissions.permissions import IsStaffOrReadOnly,IsAuthorOrReadOnly
from .models import *



class PictureViewSet(ModelViewSet):
    queryset = Pictures.objects.all()
    serializer_class = PictureSerializer
    filterset_fields = ['subjecet','category']
    search_fields = ['subjecet','category']
    # ordering_fields = ['']

    def get_permissions(self):

        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

class VideoViewSet(ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    filterset_fields = ['subjecet','category',]
    search_fields = ['subjecet','category']
    # ordering_fields = ['']

    def get_permissions(self):

        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]        