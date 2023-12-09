from typing import Dict, Any

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from src.api.v1.users.serializers import LoginUserSerializer


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        # add user details
        data["user"] = LoginUserSerializer(self.user).data
        return data


