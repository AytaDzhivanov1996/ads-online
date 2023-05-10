from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            "role",
            "password",
        )


class CurrentUserSerializer(serializers.ModelSerializer):
    current_user = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user
