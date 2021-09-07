from rest_framework import serializers

class AdobeUserCreate(serializers.Serializer):
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
    login = serializers.CharField(max_length=250)
    email = serializers.EmailField()


