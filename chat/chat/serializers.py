from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    access_token = serializers.CharField(required=True)
