from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from src.api.v1.auth.serializers import LoginSerializer


class LoginViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
