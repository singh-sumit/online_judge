from rest_framework import serializers

from src.accounts.models import User


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "mid_name", "last_name", "email")
