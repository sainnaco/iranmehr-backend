from rest_framework import serializers
from blog.models import *
from django.contrib.auth import get_user_model #اینطوری اگه یه مدل یوزر دیگه ساختیم
from drf_dynamic_fields import DynamicFieldsMixin

#روش اول و دوم دسترسی به کل فورن کی یا منی تو منی هست اما سه چهار پنج به یکی از زیر مجموعه ها
#روش اول
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id','username','first_name', 'last_name']

#روش سوم که اینجا یوزرنیم برمیگردونه
# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username

#با اضافه کردن این میکسین..فقط فیلدایی که ما مشخص میکنیم میاد
class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    # class ArticleSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Article
    #         fields = '__all__'
    #         # exclude = ('created','updated')

    #واسه یک فیلد
    def validate_title(self, value):
        filter_list = ['x','y','z']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError('not allowed :{}'.format(i))

class UserSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        # exclude = ('created','updated')

