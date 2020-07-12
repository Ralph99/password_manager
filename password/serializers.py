from rest_framework import serializers
from .models import Password


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Password
