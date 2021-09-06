from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin

User = get_user_model()


#UserCreateSerializer بازنویسی کلاس
#برای قرار دادن ایمیل بجای یوزرنیم
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')



class UserSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'        