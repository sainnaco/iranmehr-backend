from rest_framework import serializers
from .models import *
# from drf_dynamic_fields import DynamicFieldsMixin


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'

    # def validate_title(self, value):
    #     filter_list = ['x','y','z']
    #     for i in filter_list:
    #         if i in value:
    #             raise serializers.ValidationError('not allowed :{}'.format(i))

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

    # def validate_title(self, value):
    #     filter_list = ['x','y','z']
    #     for i in filter_list:
    #         if i in value:
    #             raise serializers.ValidationError('not allowed :{}'.format(i))