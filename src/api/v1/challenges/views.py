from rest_framework.viewsets import ModelViewSet

from src.api.v1.challenges.serializers import ChallengeSerializer
from src.core.models import Challenge


class ChallengeModelViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer