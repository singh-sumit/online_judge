from rest_framework.viewsets import ModelViewSet

from src.api.v1.problems.serializers import ProblemSerializer
from src.core.models import Problem


class ProblemModelViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
