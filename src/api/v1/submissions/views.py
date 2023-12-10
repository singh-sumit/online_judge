from rest_framework.viewsets import ModelViewSet

from src.api.v1.submissions.serializers import SubmissionSerializer
from src.core.models import Submission


class SubmissionModelViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer