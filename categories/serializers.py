from rest_framework import serializers
from blog.models import *
# from drf_dynamic_fields import DynamicFieldsMixin


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # def validate_title(self, value):
    #     filter_list = ['x','y','z']
    #     for i in filter_list:
    #         if i in value:
    #             raise serializers.ValidationError('not allowed :{}'.format(i))

