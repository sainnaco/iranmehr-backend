from rest_framework import serializers
from .models import *


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['signer','choose_to_send_email','choose_to_send_sms']

    def validate_content(self, value):
        return value


class FamilyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        exclude = ['signer','choose_to_send_email','choose_to_send_sms']

    def validate_content(self, value):
        return value