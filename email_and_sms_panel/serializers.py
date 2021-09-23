from rest_framework.serializers import ModelSerializer
from .models import EmailPanel ,SmsPanel


class EmailSerializer(ModelSerializer):
    class Meta:
        model = EmailPanel
        fields = '__all__'
        